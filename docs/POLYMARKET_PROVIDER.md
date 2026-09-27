# Polymarket public market-data prototype

This prototype gives Settlement Check a possible public-data fallback while Panta API access is unresolved. It is separate from the current Panta and Solana flows.

## Implemented

- Read-only Python client for Polymarket Gamma API market discovery and one market detail.
- One bounded keyset page per list call (`limit` 1–20); callers explicitly decide whether to request another page.
- Normalized records retain `provider`, source route, observation time, market question, and outcome token IDs when supplied.
- Missing fields remain null; no price or volume is inferred.
- Standard-library HTTP only, with request timeout and response validation.
- Unit tests use synthetic responses; no live API response has been validated.

## Explicitly out of scope

This is not wired into Settlement Check's CLI or catalogue. It does not fetch prices/history, trades, or order books, and has no wallet, signing, order placement, or transaction code. It does not validate Panta's API behavior or count as a Panta integration.

## References

- Market discovery: <https://docs.polymarket.com/market-data/discover-markets>
- Gamma markets: <https://docs.polymarket.com/market-data/discover-markets>
- The project-specific module and tests are in `panta_signal/providers/polymarket.py` and `tests/test_polymarket.py` in this prototype bundle.
