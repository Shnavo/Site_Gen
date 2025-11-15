import unittest

from textnode import *
from htmlnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is an test node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.LINK, "google.com")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertEqual(node.url, node3.url)
        self.assertNotEqual(node2.url, node4.url)
        self.assertNotEqual(node.text_type, node3.text_type)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.to_html(), '<a href="google.com">This is a link</a>')


if __name__ == "__main__":
    unittest.main()
