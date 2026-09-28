# Panta API Status Filter — Support Report Draft

**Status:** Draft for operator review; not sent  
**Branch:** `research/phase1-authoritative-validation-2026-09-27`  
**Date:** 2026-09-27

## Subject

`GET /api/v1/markets/` returns a `phase=primary` item when filtering for `resolved` or `cancelled`

## Summary

The documented `status` query parameter is described as a market-phase filter. In two authenticated, read-only list requests, the submitted filters were preserved in the local snapshots, but each response contained one market whose `phase` was `primary`.

## Reproduction

Using an authenticated test API key, make one request per value:

- `GET /api/v1/markets/?limit=50&status=resolved`
- `GET /api/v1/markets/?limit=50&status=cancelled`

The client and local snapshot audit confirmed those exact query values were sent. Each response had one item and a present but empty `nextCursor`. The sanitized fields from both items were:

- `phase=primary`
- `status=primary`

No market ID, title, prices, credentials, or raw response body are included in this report. The observed catalog sample currently contains one market.

## Expected behavior

The official list reference defines the filter as a phase filter and lists `primary`, `secondary`, `resolved`, and `cancelled` as accepted values. A response to `status=resolved` or `status=cancelled` should therefore contain only items with the requested `phase`, or no items if none match.

Reference: https://github.com/Kaito-HQ/panta-api-pub/blob/main/api-reference/markets/list.mdx

## Observed behavior

Both requests returned the same sampled item with `phase=primary`, which does not match either requested phase. The prior external report that these filters returned zero rows was not reproduced in this test; instead, the sample item was returned for both filters.

## Questions

1. Is `status` the correct query parameter for filtering the catalog by `phase` on the live API?
2. Is this behavior expected for test accounts or for a catalog with limited visibility?
3. Could the team confirm whether the two requests should have returned an empty `items` array?

This report describes two read-only requests from a single-market sample and does not claim catalog-wide impact.
