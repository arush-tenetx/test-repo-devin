import subprocess
import sys
import unittest
from pathlib import Path

from sum_numbers import add

SCRIPT = Path(__file__).with_name("sum_numbers.py")


class TestScriptOutput(unittest.TestCase):
    def run_script(self, first, second):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            input=f"{first}\n{second}\n",
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout

    def test_integer_inputs_print_integer_sum(self):
        self.assertIn("Sum: 5\n", self.run_script(2, 3))

    def test_decimal_inputs_print_decimal_sum(self):
        self.assertIn("Sum: 3.75\n", self.run_script(1.5, 2.25))


class TestAdd(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_integers(self):
        self.assertEqual(add(-4, -6), -10)

    def test_mixed_signs(self):
        self.assertEqual(add(-2, 7), 5)

    def test_with_zero(self):
        self.assertEqual(add(0, 9), 9)
        self.assertEqual(add(9, 0), 9)

    def test_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_large_numbers(self):
        self.assertEqual(add(10**12, 10**12), 2 * 10**12)


if __name__ == "__main__":
    unittest.main()
