"""Provisional deterministic calculations over preserved Panta observations.

These outputs describe source fields only; they do not assign probability semantics
to Panta's yesPrice field.
"""

from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation


def _market_observations(record, market_id):
    response = record.get("response", {})
    candidates = []
    items = response.get("items", [])
    if isinstance(items, list):
        candidates.extend(items)

    market = response.get("market")
    if isinstance(market, dict):
        candidates.append({"marketId": market.get("marketId"), "market": market})

    for item in candidates:
        if not isinstance(item, dict):
            continue
        market_data = item.get("market")
        if not isinstance(market_data, dict):
            continue
        item_market_id = item.get("marketId") or market_data.get("marketId")
        if item_market_id != market_id:
            continue

        value = market_data.get("yesPrice")
        if isinstance(value, bool) or value is None:
            raise ValueError("matching observation is missing a valid yesPrice")
        try:
            price = Decimal(str(value))
        except (InvalidOperation, ValueError) as exc:
            raise ValueError("matching observation has malformed yesPrice") from exc
        if not price.is_finite():
            raise ValueError("matching observation has non-finite yesPrice")

        observed_at = response.get("observedAt")
        if not isinstance(observed_at, str) or not observed_at:
            raise ValueError("matching observation is missing observedAt")
        try:
            timestamp = datetime.fromisoformat(observed_at.replace("Z", "+00:00"))
        except ValueError as exc:
            raise ValueError("matching observation has malformed observedAt") from exc
        if timestamp.tzinfo is None or timestamp.utcoffset() is None:
            raise ValueError("observedAt must include a timezone")

        yield {
            "timestamp": timestamp.astimezone(timezone.utc),
            "observedAt": observed_at,
            "value": price,
            "sourceRoute": response.get("sourceRoute"),
        }


def _decimal_text(value):
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def calculate_source_price_delta(records, market_id):
    """Calculate first-to-last yesPrice delta for one market from snapshots.

    The result is a provisional source-field movement measure, not a validated
    probability or trading recommendation. Records with no matching market are
    ignored. At least two timezone-aware observations are required.
    """
    if not isinstance(market_id, str) or not market_id.strip():
        raise ValueError("market_id must be a non-empty string")

    observations = []
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("snapshot record must be an object")
        observations.extend(_market_observations(record, market_id))

    observations.sort(key=lambda item: (item["timestamp"], item["observedAt"]))
    timestamps = [item["timestamp"] for item in observations]
    if len(timestamps) != len(set(timestamps)):
        raise ValueError("matching observations contain duplicate timestamps")

    result = {
        "algorithm": "source-price-delta",
        "version": 1,
        "marketId": market_id,
        "sourceField": "yesPrice",
        "status": "insufficient",
        "observationCount": len(observations),
        "startObservedAt": None,
        "endObservedAt": None,
        "startValue": None,
        "endValue": None,
        "delta": None,
        "direction": None,
        "startSourceRoute": None,
        "endSourceRoute": None,
    }
    if len(observations) < 2:
        return result

    start = observations[0]
    end = observations[-1]
    delta = end["value"] - start["value"]
    result.update(
        {
            "status": "sufficient",
            "startObservedAt": start["observedAt"],
            "endObservedAt": end["observedAt"],
            "startValue": _decimal_text(start["value"]),
            "endValue": _decimal_text(end["value"]),
            "delta": _decimal_text(delta),
            "direction": "up" if delta > 0 else "down" if delta < 0 else "unchanged",
            "startSourceRoute": start["sourceRoute"],
            "endSourceRoute": end["sourceRoute"],
        }
    )
    return result
