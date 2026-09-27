import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

try:
    from panta_signal.providers.panta import PantaReadClient, ProviderError
except ModuleNotFoundError:
    PantaReadClient = None
    ProviderError = ValueError


class PantaReadClientTests(unittest.TestCase):
    def client_type(self):
        if PantaReadClient is None:
            self.fail("Panta read client is not implemented")
        return PantaReadClient

    def create_client(self, responses):
        calls = []

        def runner(args, **kwargs):
            calls.append((args, kwargs))
            return responses.pop(0)

        return self.client_type()("pk_test_synthetic", runner=runner), calls

    @staticmethod
    def response(body, status=200, returncode=0):
        return SimpleNamespace(
            stdout=f"{json.dumps(body)}\nPANTA_HTTP_STATUS:{status}",
            stderr="",
            returncode=returncode,
        )

    def test_categories_uses_get_and_keeps_key_out_of_process_arguments(self):
        client, calls = self.create_client([
            self.response({"categories": ["crypto", "sports"]})
        ])

        result = client.get_categories()

        args, kwargs = calls[0]
        config = kwargs["input"]
        self.assertEqual(args, ["curl", "-q", "--config", "-"])
        self.assertIn('request = "GET"', config)
        self.assertIn("X-Api-Key: pk_test_synthetic", config)
        self.assertNotIn("pk_test_synthetic", " ".join(args))
        self.assertEqual(result["categories"], ["crypto", "sports"])
        self.assertEqual(result["sourceRoute"], "/categories/")

    def test_list_preserves_sparse_fields_and_null_cursor(self):
        raw_market = {"marketId": "synthetic-market", "title": "Synthetic", "phase": "primary", "onChain": False}
        client, _calls = self.create_client([
            self.response({"items": [raw_market], "nextCursor": None})
        ])

        page = client.list_markets(limit=2)

        market = page["items"][0]
        self.assertEqual(market["marketId"], "synthetic-market")
        self.assertEqual(market["market"], raw_market)
        self.assertNotIn("question", market["market"])
        self.assertNotIn("question", market["presentFields"])
        self.assertTrue(page["cursorPresent"])
        self.assertIsNone(page["nextCursor"])

    def test_detail_does_not_invent_optional_fields(self):
        raw_market = {"marketId": "synthetic-market", "title": "Synthetic", "phase": "primary", "onChain": True}
        client, _calls = self.create_client([self.response(raw_market)])

        result = client.get_market("synthetic-market")

        self.assertEqual(result["market"], raw_market)
        self.assertNotIn("resolutionRule", result["market"])
        self.assertIn("onChain", result["presentFields"])

    def test_empty_trade_tape_is_valid_and_preserved(self):
        client, _calls = self.create_client([
            self.response({"marketId": "synthetic-market", "items": []})
        ])

        result = client.get_trades("synthetic-market", limit=10)

        self.assertEqual(result["trades"], [])
        self.assertEqual(result["marketId"], "synthetic-market")

    def test_market_list_limit_is_bounded_before_network(self):
        client, calls = self.create_client([])

        with self.assertRaises(ProviderError):
            client.list_markets(limit=51)
        self.assertEqual(calls, [])

    def test_http_error_does_not_expose_api_key(self):
        client, _calls = self.create_client([
            self.response({"code": "FORBIDDEN", "message": "denied"}, status=403)
        ])

        with self.assertRaises(ProviderError) as raised:
            client.get_categories()
        self.assertIn("HTTP 403", str(raised.exception))
        self.assertNotIn("pk_test_synthetic", str(raised.exception))


if __name__ == "__main__":
    unittest.main()
