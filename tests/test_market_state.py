import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from panta_signal.market_state import classify_on_chain


class OnChainClassificationTests(unittest.TestCase):
    def test_missing_field_is_unknown_and_distinguished(self):
        self.assertEqual(
            classify_on_chain({"marketId": "synthetic"}),
            {"state": "unknown", "sourceFieldState": "missing"},
        )

    def test_explicit_null_is_unknown_and_distinguished(self):
        self.assertEqual(
            classify_on_chain({"onChain": None}),
            {"state": "unknown", "sourceFieldState": "null"},
        )

    def test_explicit_true_is_reported_on_chain(self):
        self.assertEqual(
            classify_on_chain({"onChain": True}),
            {"state": "reported_on_chain", "sourceFieldState": "boolean"},
        )

    def test_explicit_false_is_reported_off_chain(self):
        self.assertEqual(
            classify_on_chain({"onChain": False}),
            {"state": "reported_off_chain", "sourceFieldState": "boolean"},
        )

    def test_non_boolean_is_unknown_without_coercion(self):
        for value in ("true", "false", 0, 1, []):
            with self.subTest(value_type=type(value).__name__):
                self.assertEqual(
                    classify_on_chain({"onChain": value}),
                    {"state": "unknown", "sourceFieldState": "non_boolean"},
                )

    def test_source_object_is_not_mutated(self):
        source = {"onChain": None}
        before = dict(source)
        classify_on_chain(source)
        self.assertEqual(source, before)

    def test_non_object_market_is_rejected(self):
        for value in (None, [], "market"):
            with self.subTest(value_type=type(value).__name__):
                with self.assertRaises(TypeError):
                    classify_on_chain(value)


if __name__ == "__main__":
    unittest.main()
