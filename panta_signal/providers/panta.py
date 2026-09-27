"""Read-only client for Panta's public market-data endpoints.

The client only sends GET requests. It uses the documented X-Api-Key header,
passes credentials to curl over stdin, and never places them in URLs or logs.
"""

import json
import re
import subprocess
from datetime import datetime, timezone
from urllib.parse import quote, urlencode


LIVE_API_BASE = "https://live-api.panta.market/api/v1"
STAGING_API_BASE = "https://staging-api.panta.market/api/v1"
_API_BASES = {LIVE_API_BASE, STAGING_API_BASE}
_API_KEY_PATTERN = re.compile(r"^pk_(?:test|live)_[A-Za-z0-9_-]+$")
_STATUS_MARKER = "\nPANTA_HTTP_STATUS:"


class ProviderError(RuntimeError):
    """Raised when a Panta response is unavailable or malformed."""


def _timestamp():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _normalize_market(raw, route):
    if not isinstance(raw, dict):
        raise ProviderError("market entry must be an object")
    market_id = raw.get("marketId")
    if not isinstance(market_id, str) or not market_id.strip():
        raise ProviderError("marketId must be a non-empty string")
    return {
        "provider": "panta",
        "marketId": market_id,
        "market": dict(raw),
        "presentFields": sorted(raw),
        "sourceRoute": route,
        "observedAt": _timestamp(),
    }


class PantaReadClient:
    """Bounded read-only access to Panta categories, markets, and trades."""

    def __init__(self, api_key, *, base_url=LIVE_API_BASE, timeout=10, runner=None):
        if not isinstance(api_key, str) or not _API_KEY_PATTERN.fullmatch(api_key):
            raise ProviderError("api_key must be a Panta test or live key")
        if base_url not in _API_BASES:
            raise ProviderError("base_url must be an official Panta API base")
        if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or timeout <= 0:
            raise ProviderError("timeout must be greater than zero")
        self._api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._runner = runner or subprocess.run

    @staticmethod
    def _config_quote(value):
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'

    def _get_json(self, route):
        url = self.base_url + route
        config = "\n".join(
            (
                f"url = {self._config_quote(url)}",
                'request = "GET"',
                'header = "Accept: application/json"',
                f'header = {self._config_quote("X-Api-Key: " + self._api_key)}',
                f"max-time = {self.timeout}",
                "silent = true",
                "show-error = true",
                'write-out = "\\nPANTA_HTTP_STATUS:%{http_code}"',
                "",
            )
        )
        try:
            result = self._runner(
                # Keep -q first so user-level curlrc options cannot inject
                # arguments or break parsing in Termux and other shells.
                ["curl", "-q", "--config", "-"],
                input=config,
                capture_output=True,
                text=True,
                timeout=self.timeout + 2,
                check=False,
            )
        except FileNotFoundError as exc:
            raise ProviderError("curl executable is unavailable") from exc
        except subprocess.TimeoutExpired as exc:
            raise ProviderError("Panta request timed out") from exc
        if result.returncode != 0:
            raise ProviderError("Panta request failed at the HTTP transport")
        if _STATUS_MARKER not in result.stdout:
            raise ProviderError("Panta response did not include an HTTP status")

        body, status_text = result.stdout.rsplit(_STATUS_MARKER, 1)
        try:
            status = int(status_text.strip())
        except ValueError as exc:
            raise ProviderError("Panta returned an invalid HTTP status") from exc
        try:
            payload = json.loads(body)
        except json.JSONDecodeError as exc:
            raise ProviderError("Panta returned invalid JSON") from exc
        if not 200 <= status < 300:
            code = payload.get("code") if isinstance(payload, dict) else None
            suffix = f" ({code})" if isinstance(code, str) else ""
            raise ProviderError(f"Panta returned HTTP {status}{suffix}")
        return payload

    def get_categories(self):
        """Return the documented category allowlist."""
        route = "/categories/"
        payload = self._get_json(route)
        categories = payload.get("categories") if isinstance(payload, dict) else None
        if not isinstance(categories, list) or any(not isinstance(x, str) for x in categories):
            raise ProviderError("categories response must contain a string array")
        return {
            "provider": "panta",
            "sourceRoute": route,
            "observedAt": _timestamp(),
            "categories": list(categories),
        }

    def list_markets(self, *, limit=20, cursor=None, category=None, status=None):
        """Fetch one page only; callers decide whether to request another."""
        if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 50:
            raise ProviderError("limit must be an integer between 1 and 50")
        params = {"limit": limit}
        for name, value in (("cursor", cursor), ("category", category), ("status", status)):
            if value is not None:
                if not isinstance(value, str) or not value.strip():
                    raise ProviderError(f"{name} must be a non-empty string or null")
                params[name] = value
        route = "/markets/?" + urlencode(params)
        payload = self._get_json(route)
        if not isinstance(payload, dict) or not isinstance(payload.get("items"), list):
            raise ProviderError("market list response must contain an items array")
        cursor_present = "nextCursor" in payload
        next_cursor = payload.get("nextCursor")
        if next_cursor is not None and not isinstance(next_cursor, str):
            raise ProviderError("nextCursor must be a string or null")
        return {
            "provider": "panta",
            "sourceRoute": route,
            "observedAt": _timestamp(),
            "items": [_normalize_market(item, route) for item in payload["items"]],
            "cursorPresent": cursor_present,
            "nextCursor": next_cursor,
        }

    def get_market(self, market_id):
        """Fetch one market detail without filling omitted source fields."""
        if not isinstance(market_id, str) or not market_id.strip():
            raise ProviderError("market_id must be a non-empty string")
        route = "/markets/" + quote(market_id, safe="") + "/"
        result = _normalize_market(self._get_json(route), route)
        result["observedAt"] = _timestamp()
        return result

    def get_trades(self, market_id, *, limit=50):
        """Fetch one bounded trade-tape page; an empty items array is valid."""
        if not isinstance(market_id, str) or not market_id.strip():
            raise ProviderError("market_id must be a non-empty string")
        if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 200:
            raise ProviderError("limit must be an integer between 1 and 200")
        route = "/markets/" + quote(market_id, safe="") + "/trades/?" + urlencode({"limit": limit})
        payload = self._get_json(route)
        if not isinstance(payload, dict) or not isinstance(payload.get("items"), list):
            raise ProviderError("trade response must contain an items array")
        for row in payload["items"]:
            if not isinstance(row, dict):
                raise ProviderError("trade rows must be objects")
            row_market_id = row.get("marketId")
            if row_market_id is not None and row_market_id != market_id:
                raise ProviderError("trade row marketId does not match the requested market")
        response_market_id = payload.get("marketId")
        if response_market_id is not None and response_market_id != market_id:
            raise ProviderError("trade response marketId does not match the request")
        return {
            "provider": "panta",
            "marketId": market_id,
            "sourceRoute": route,
            "observedAt": _timestamp(),
            "trades": list(payload["items"]),
            "presentFields": sorted(payload),
        }
