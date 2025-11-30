import unittest

from page_creators import *


class Testpagecreator(unittest.TestCase):
    def test_extract_header(self):
        markdown = """
# This is the first header

## This is a second header

This is not a header
"""
        header = extract_title(markdown)
        self.assertEqual(
            header,
            "This is the first header",
        )

    def test_no_headers(self):
        markdown = """
There is no header here

or anywhere in this tester
"""
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_no_first_header(self):
        markdown = """
## There is a second header here

and no headers in here
"""
        with self.assertRaises(Exception):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()
