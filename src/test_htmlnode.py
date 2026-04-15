import unittest

from htmlnode import HTMLNode


def test_props_to_html(self):
    node = HTMLNode("a", "click me", None, {"href": "https://google.com"})
    self.assertEqual(node.props_to_html(), ' href="https://google.com"')

def test_props_none(self):
    node = HTMLNode("a", "click me", None, None)
    self.assertEqual(node.props_to_html(), '')

def test_props_empty(self):
    node = HTMLNode("a", "click me", None, {})
    self.assertEqual(node.props_to_html(), '')

def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

def test_leaf_to_html_None(self):
    node = LeafNode(None, "Hello, world!")
    self.assertEqual(node.to_html(), "Hello, world!")

def test_leaf_to_html_props(self):
    node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
    self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')

def test_leaf_to_html_ValueError(self):
    node = LeafNode("p", None)
    with self.assertRaises(ValueError):
        node.to_html()

if __name__ == "__main__":
    unittest.main()