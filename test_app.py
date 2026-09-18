import unittest
from unittest.mock import patch

import app


class TestSalesTracker(unittest.TestCase):

    def test_load_config(self):
        config = app.load_config()

        self.assertIn("currency", config)

    def test_summary(self):
        records = [
            {
                "customer": "Ali",
                "product": "Keyboard",
                "amount": 2500
            },
            {
                "customer": "Sara",
                "product": "Mouse",
                "amount": 1500
            }
        ]

        with patch("builtins.print") as mock_print:
            app.show_summary(records, "PKR")

            output = " ".join(
                str(call) for call in mock_print.call_args_list
            )

            self.assertIn("4,000.00", output)


if __name__ == "__main__":
    unittest.main()