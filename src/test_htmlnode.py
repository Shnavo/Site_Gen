import unittest

from htmlnode import *


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

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )
        self.assertEqual(node, node2)




if __name__ == "__main__":
    unittest.main()