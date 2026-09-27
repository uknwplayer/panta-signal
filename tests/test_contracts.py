import json
import sys
import unittest
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

try:
    from panta_signal.contracts import ContractError, validate_synthetic_fixture
except ModuleNotFoundError:
    ContractError = ValueError
    validate_synthetic_fixture = None

FIXTURES = ROOT / "fixtures" / "panta" / "v0-provisional"


def read_fixture(name):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class SyntheticFixtureContractTests(unittest.TestCase):
    def validate(self, value):
        if validate_synthetic_fixture is None:
            self.fail("synthetic fixture validator is not implemented")
        return validate_synthetic_fixture(value)

    def test_market_list_keeps_missing_prices_as_null(self):
        fixture = read_fixture("market-list.synthetic.json")

        validated = self.validate(fixture)

        self.assertIsNone(validated["market"]["yesPrice"])
        self.assertIsNone(validated["market"]["noPrice"])

    def test_market_detail_preserves_decimal_strings(self):
        fixture = read_fixture("market-detail.synthetic.json")

        validated = self.validate(fixture)

        self.assertEqual(validated["market"]["yesPrice"], "0.58")
        self.assertEqual(validated["market"]["noPrice"], "0.42")

    def test_trade_fixture_preserves_signature_and_market_link(self):
        fixture = read_fixture("trades.synthetic.json")

        validated = self.validate(fixture)

        self.assertEqual(validated["trades"][0]["transactionSignature"], "synthetic-signature-001")
        self.assertEqual(validated["trades"][0]["marketId"], validated["marketId"])

    def test_fixture_cannot_claim_live_validation(self):
        fixture = read_fixture("market-list.synthetic.json")
        fixture["liveValidated"] = True

        with self.assertRaises(ContractError):
            self.validate(fixture)

    def test_market_observation_requires_source_market_id(self):
        fixture = read_fixture("market-list.synthetic.json")
        del fixture["market"]["marketId"]

        with self.assertRaises(ContractError):
            self.validate(fixture)

    def test_market_observation_rejects_malformed_decimal(self):
        fixture = read_fixture("market-list.synthetic.json")
        fixture["market"]["volumeUsdc"] = "one hundred"

        with self.assertRaises(ContractError):
            self.validate(fixture)

    def test_trade_must_belong_to_fixture_market(self):
        fixture = deepcopy(read_fixture("trades.synthetic.json"))
        fixture["trades"][0]["marketId"] = "fixture-market-other"

        with self.assertRaises(ContractError):
            self.validate(fixture)


if __name__ == "__main__":
    unittest.main()
