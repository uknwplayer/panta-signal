"""Read-only client for Polymarket's public market-data endpoints.

This module only issues GET requests. It does not implement CLOB order,
wallet, signing, or transaction endpoints.
"""

import json
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


API_BASE = "https://gamma-api.polymarket.com"


class ProviderError(RuntimeError):
    """Raised when a provider response is unavailable or malformed."""


def _optional_string(value, field):
    if value is None:
        return None
    if not isinstance(value, str):
        raise ProviderError(f"{field} must be a string or null")
    return value


def _array_value(value, field):
    if value is None:
        return None
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except json.JSONDecodeError as exc:
            raise ProviderError(f"{field} must contain a JSON array") from exc
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ProviderError(f"{field} must be an array of strings")
    return value


def normalize_market(raw, route):
    """Return a source-labelled record without inventing absent market data."""
    if not isinstance(raw, dict):
        raise ProviderError("market entry must be an object")

    market_id = raw.get("id")
    if isinstance(market_id, bool) or not isinstance(market_id, (str, int)):
        raise ProviderError("market id must be a string or integer")
    market_id = str(market_id).strip()
    if not market_id:
        raise ProviderError("market id must be non-empty")

    outcomes = _array_value(raw.get("outcomes"), "outcomes")
    token_ids = _array_value(raw.get("clobTokenIds"), "clobTokenIds")
    outcome_token_ids = {}
    if outcomes is not None and token_ids is not None:
        if len(outcomes) != len(token_ids):
            raise ProviderError("outcomes and clobTokenIds must have matching lengths")
        outcome_token_ids = {
            outcome.strip().casefold(): token_id
            for outcome, token_id in zip(outcomes, token_ids)
        }

    slug = _optional_string(raw.get("slug"), "slug")
    question = _optional_string(raw.get("question"), "question")
    condition_id = _optional_string(raw.get("conditionId"), "conditionId")
    active = raw.get("active")
    closed = raw.get("closed")
    if active is not None and not isinstance(active, bool):
        raise ProviderError("active must be a boolean or null")
    if closed is not None and not isinstance(closed, bool):
        raise ProviderError("closed must be a boolean or null")

    return {
        "provider": "polymarket",
        "marketId": market_id,
        "slug": slug,
        "question": question,
        "conditionId": condition_id,
        "active": active,
        "closed": closed,
        "outcomeTokenIds": outcome_token_ids,
        "marketUrl": (
            f"https://polymarket.com/market/{quote(slug, safe='-')}" if slug else None
        ),
        "sourceRoute": route,
        "observedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }


class PolymarketReadClient:
    """Minimal public reader for active markets and market details."""

    def __init__(self, opener=None, timeout=5):
        if not isinstance(timeout, (int, float)) or timeout <= 0:
            raise ProviderError("timeout must be greater than zero")
        self._opener = opener or urlopen
        self.timeout = timeout

    def _get_json(self, url):
        request = Request(
            url,
            headers={"Accept": "application/json", "User-Agent": "PantaSignal/0.1"},
            method="GET",
        )
        try:
            with self._opener(request, timeout=self.timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            raise ProviderError(f"Polymarket returned HTTP {exc.code}") from exc
        except (URLError, TimeoutError) as exc:
            raise ProviderError("Polymarket market-data request failed") from exc
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ProviderError("Polymarket returned invalid JSON") from exc

    def list_markets(self, limit=20, after_cursor=None):
        """Fetch one bounded keyset page; callers control any subsequent read."""
        if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 20:
            raise ProviderError("limit must be an integer between 1 and 20")
        if after_cursor is not None and (
            not isinstance(after_cursor, str) or not after_cursor.strip()
        ):
            raise ProviderError("after_cursor must be a non-empty string or null")

        params = {"closed": "false", "limit": limit}
        if after_cursor is not None:
            params["after_cursor"] = after_cursor
        route = "/markets/keyset?" + urlencode(params)
        response = self._get_json(API_BASE + route)
        if not isinstance(response, dict) or not isinstance(response.get("markets"), list):
            raise ProviderError("market page must contain a markets array")
        next_cursor = response.get("next_cursor")
        if next_cursor is not None and not isinstance(next_cursor, str):
            raise ProviderError("next_cursor must be a string or null")
        return {
            "provider": "polymarket",
            "sourceRoute": route,
            "markets": [normalize_market(item, route) for item in response["markets"]],
            "nextCursor": next_cursor,
        }

    def get_market(self, market_id):
        """Fetch one public market detail by ID; never performs trading actions."""
        if not isinstance(market_id, (str, int)) or isinstance(market_id, bool):
            raise ProviderError("market id must be a string or integer")
        market_id = str(market_id).strip()
        if not market_id:
            raise ProviderError("market id must be non-empty")
        route = "/markets/" + quote(market_id, safe="")
        response = self._get_json(API_BASE + route)
        return normalize_market(response, route)
