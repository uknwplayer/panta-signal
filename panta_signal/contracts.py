"""Validation for synthetic Panta fixtures, not captured live responses.

The provider has limited live observations, but this validator does not assert
that the provisional fixture contract matches all upstream response shapes.
"""

from datetime import datetime
from decimal import Decimal, InvalidOperation


class ContractError(ValueError):
    """Raised when a provisional synthetic fixture violates its contract."""


def _nonempty_string(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{field} must be a non-empty string")


def _decimal_string_or_none(value, field):
    if value is None:
        return
    if not isinstance(value, str):
        raise ContractError(f"{field} must be a decimal string or null")
    try:
        parsed = Decimal(value)
    except InvalidOperation as exc:
        raise ContractError(f"{field} must be a decimal string or null") from exc
    if not parsed.is_finite():
        raise ContractError(f"{field} must be finite")


def _timestamp(value, field):
    _nonempty_string(value, field)
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ContractError(f"{field} must be an ISO-8601 timestamp") from exc
    if parsed.tzinfo is None:
        raise ContractError(f"{field} must include a timezone")


def _validate_market(document):
    market = document.get("market")
    if not isinstance(market, dict):
        raise ContractError("market must be an object")

    for field in ("marketId", "title", "phase"):
        _nonempty_string(market.get(field), f"market.{field}")
    for field in ("category", "marketType"):
        value = market.get(field)
        if value is not None and not isinstance(value, str):
            raise ContractError(f"market.{field} must be a string or null")
    for field in ("volumeUsdc", "yesPrice", "noPrice"):
        _decimal_string_or_none(market.get(field), f"market.{field}")


def _validate_trades(document):
    market_id = document.get("marketId")
    _nonempty_string(market_id, "marketId")
    trades = document.get("trades")
    if not isinstance(trades, list):
        raise ContractError("trades must be an array")

    for index, trade in enumerate(trades):
        prefix = f"trades[{index}]"
        if not isinstance(trade, dict):
            raise ContractError(f"{prefix} must be an object")
        if trade.get("marketId") != market_id:
            raise ContractError(f"{prefix}.marketId must match the fixture marketId")
        for field in ("transactionSignature", "phase", "quoteAsset"):
            _nonempty_string(trade.get(field), f"{prefix}.{field}")
        for field in ("yesShareAmount", "noShareAmount", "fee"):
            _decimal_string_or_none(trade.get(field), f"{prefix}.{field}")
            if trade.get(field) is None:
                raise ContractError(f"{prefix}.{field} cannot be null")
        _timestamp(trade.get("blockTime"), f"{prefix}.blockTime")


def validate_synthetic_fixture(document):
    """Validate and return one explicitly synthetic provisional fixture."""
    if not isinstance(document, dict):
        raise ContractError("fixture must be a JSON object")
    if document.get("fixtureStatus") != "synthetic_not_provider_response":
        raise ContractError("fixture must be explicitly marked synthetic")
    if document.get("liveValidated") is not False:
        raise ContractError("synthetic fixture cannot claim live validation")
    version = document.get("schemaVersion")
    if not isinstance(version, str) or not version.endswith(".v0-provisional"):
        raise ContractError("schemaVersion must identify the provisional contract")
    if document.get("provider") != "panta":
        raise ContractError("provider must be panta")
    _nonempty_string(document.get("route"), "route")
    if not document["route"].startswith("/"):
        raise ContractError("route must be a relative API path")
    _timestamp(document.get("fetchedAt"), "fetchedAt")

    if version.startswith("panta-signal.market-observation."):
        _validate_market(document)
    elif version.startswith("panta-signal.trade-tape."):
        _validate_trades(document)
    else:
        raise ContractError("unsupported provisional fixture type")
    return document
