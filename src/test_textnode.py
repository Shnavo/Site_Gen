import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()