import unittest

from blocks import markdown_to_blocks, block_to_block_type, BlockType


class TestMarkdownBlocks(unittest.TestCase):
    def test_text_to_blocks(self):
        md = "This is **bolded** paragraph\n\nThis is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\n\n- This is a list\n- with items"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_bad_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list

- with items


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list",
                "- with items",
            ],
        )


class TestBlockTypes(unittest.TestCase):
    def test_heading(self):
        block1 = """
# this is the first heading
"""
        block2 = """
### this is a 3rd heading
"""
        block3 = """
####### this should not be a heading
"""
        self.assertEqual(block_to_block_type(block1), BlockType.HEADING)
        self.assertEqual(block_to_block_type(block2), BlockType.HEADING)
        self.assertNotEqual(block_to_block_type(block3), BlockType.HEADING)

    def test_code(self):
        block = """
```test code```
"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_quote(self):
        block = """
>first line of quote
> second line of quote
"""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_unordered(self):
        block = """
- first point of an unordered list
- second point of an unordered list
"""
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered(self):
        block = """
1. first point of an unordered list
2. second point of an unordered list
"""
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()
