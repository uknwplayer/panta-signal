import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

try:
    from panta_signal.providers.polymarket import (
        PolymarketReadClient,
        ProviderError,
    )
except ModuleNotFoundError:
    PolymarketReadClient = None
    ProviderError = ValueError


class FakeResponse:
    def __init__(self, value):
        self.body = json.dumps(value).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return self.body


class PolymarketReadClientTests(unittest.TestCase):
    def create_client(self, replies):
        requests = []

        def opener(request, timeout):
            requests.append((request, timeout))
            return FakeResponse(replies.pop(0))

        client = self.client_type()(opener=opener)
        return client, requests

    def client_type(self):
        if PolymarketReadClient is None:
            self.fail("Polymarket read client is not implemented")
        return PolymarketReadClient

    def test_list_markets_uses_public_get_and_preserves_next_cursor(self):
        client, requests = self.create_client([{
            "markets": [{
                "id": "market-42",
                "slug": "will-it-happen",
                "question": "Will it happen?",
                "conditionId": "condition-42",
            }],
            "next_cursor": "cursor-2",
        }])

        page = client.list_markets(limit=7)

        request, timeout = requests[0]
        self.assertEqual(request.get_method(), "GET")
        self.assertNotIn("Authorization", request.headers)
        self.assertIn("/markets/keyset?", request.full_url)
        self.assertIn("closed=false", request.full_url)
        self.assertIn("limit=7", request.full_url)
        self.assertEqual(timeout, 5)
        self.assertEqual(page["nextCursor"], "cursor-2")
        self.assertEqual(page["markets"][0]["provider"], "polymarket")
        self.assertEqual(page["markets"][0]["marketId"], "market-42")
        self.assertEqual(page["markets"][0]["question"], "Will it happen?")

    def test_list_markets_passes_cursor_without_automatic_extra_reads(self):
        client, requests = self.create_client([{"markets": [], "next_cursor": None}])

        page = client.list_markets(limit=3, after_cursor="cursor-2")

        self.assertEqual(len(requests), 1)
        self.assertIn("after_cursor=cursor-2", requests[0][0].full_url)
        self.assertIsNone(page["nextCursor"])

    def test_get_market_maps_yes_and_no_token_ids(self):
        client, requests = self.create_client([{
            "id": "market-42",
            "slug": "will-it-happen",
            "question": "Will it happen?",
            "conditionId": "condition-42",
            "outcomes": "[\"Yes\", \"No\"]",
            "clobTokenIds": "[\"yes-token\", \"no-token\"]",
        }])

        market = client.get_market("market-42")

        self.assertEqual(requests[0][0].get_method(), "GET")
        self.assertEqual(requests[0][0].full_url, "https://gamma-api.polymarket.com/markets/market-42")
        self.assertEqual(market["outcomeTokenIds"], {"yes": "yes-token", "no": "no-token"})

    def test_list_markets_rejects_malformed_envelope(self):
        client, _requests = self.create_client([{"results": []}])

        with self.assertRaises(ProviderError):
            client.list_markets()

    def test_market_id_must_be_nonempty(self):
        with self.assertRaises(ProviderError):
            self.client_type()().get_market(" ")

    def test_limit_is_bounded(self):
        client, requests = self.create_client([{"markets": []}])

        with self.assertRaises(ProviderError):
            client.list_markets(limit=0)
        self.assertEqual(requests, [])


if __name__ == "__main__":
    unittest.main()
