import unittest

from gencontent import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        result = extract_title("# Some Title")
        self.assertEqual(result, "Some Title")