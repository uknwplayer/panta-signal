"""Consumer-facing classification for sparse Panta onChain fields.

This is a derived view only. It never rewrites the provider snapshot.
"""


def classify_on_chain(market):
    """Classify an onChain field without treating missing/null as false.

    Returns a small derived object with:
    - state: reported_on_chain, reported_off_chain, or unknown;
    - sourceFieldState: missing, null, boolean, or non_boolean.

    The caller should retain the original market object and its presentFields.
    """
    if not isinstance(market, dict):
        raise TypeError("market must be an object")

    if "onChain" not in market:
        return {"state": "unknown", "sourceFieldState": "missing"}

    value = market["onChain"]
    if value is None:
        return {"state": "unknown", "sourceFieldState": "null"}
    if type(value) is bool:
        return {
            "state": "reported_on_chain" if value else "reported_off_chain",
            "sourceFieldState": "boolean",
        }
    return {"state": "unknown", "sourceFieldState": "non_boolean"}
