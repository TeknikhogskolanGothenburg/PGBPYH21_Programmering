import unittest
from unittest.mock import patch
from io import StringIO
import sys
from contextlib import contextmanager
from main import get_third_letter_from_input, print_third_letter


class CaptureOutput:
    def __init__(self):
        self.new_out = StringIO()
        self.new_err = StringIO()
        self.old_out = sys.stdout
        self.old_err = sys.stderr

    def __enter__(self):
        sys.stdout = self.new_out
        sys.stderr = self.new_err
        return sys.stdout, sys.stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.old_out
        sys.stderr = self.old_err
        return True


@contextmanager
def capture_output():
    new_out = StringIO()
    new_err = StringIO()
    old_out = sys.stdout
    old_err = sys.stderr
    try:
        sys.stdout = new_out
        sys.stderr = new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout = old_out
        sys.stderr = old_err


class TDDTestCase(unittest.TestCase):
    def test_j_get_third_letter_from_input(self):
        with patch('builtins.input', return_value="hej"):
            letter = get_third_letter_from_input()
        self.assertEqual("j", letter)

    def test_p_get_third_letter_from_input(self):
        with patch('builtins.input', return_value="hepp"):
            letter = get_third_letter_from_input()
        self.assertEqual("p", letter)

    def test_less_than_3_third_letter_from_input(self):
        with patch('builtins.input', return_value="sa"):
            with self.assertRaises(ValueError):
                letter = get_third_letter_from_input()

    def test_output_j_of_third_letter_from_input(self):
        with patch('builtins.input', return_value="Hon sa hej till mig"):
            with capture_output() as (out, err):
                print_third_letter()
        printed = out.getvalue()
        printed = printed.split()[-1]
        self.assertEqual('n', printed)


if __name__ == '__main__':
    unittest.main()
