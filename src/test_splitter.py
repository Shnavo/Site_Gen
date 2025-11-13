import unittest
from splitter import *

class Testsplitterfunction(unittest.TestCase):
    def test_function(self):
        code_node = TextNode("This is text with a `code block` word", TextType.TEXT)
        italics_node = TextNode("This is text with an _italicized_ word", TextType.TEXT)
        bolded_node = TextNode("This is text with a *bolded* word", TextType.TEXT)
        code_nodes = split_nodes_delimiter([code_node], "`", TextType.CODE)
        italics_nodes = split_nodes_delimiter([italics_node], "_", TextType.ITALIC)
        bolded_nodes = split_nodes_delimiter([bolded_node], "*", TextType.BOLD)
        self.assertEqual(
            code_nodes, 
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )
        self.assertEqual(
            italics_nodes, 
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italicized", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ]
        )
        self.assertEqual(
            bolded_nodes, 
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ]
        )
    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()