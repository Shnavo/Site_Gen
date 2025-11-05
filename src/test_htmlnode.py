import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a test node", props = {"href":"https://www.google.com"})
        node2 = HTMLNode("p", "This is a test node", props = {"href":"https://www.google.com"})
        node3 = HTMLNode("a1", "This is an test node", [node, node2])
        node4 = HTMLNode("a", "This is a test node", props = {"target": "_blank"})
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertEqual(node.value, node4.value)
        self.assertNotEqual(node2.tag, node4.tag)
        self.assertNotEqual(node.children, node3.children)
        self.assertEqual(node.props_to_html(), node2.props_to_html())
        self.assertNotEqual(node.props_to_html(), node3.props_to_html())
        self.assertNotEqual(node2.props_to_html(), node3.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')


if __name__ == "__main__":
    unittest.main()