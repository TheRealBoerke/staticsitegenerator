import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    # Purpose: Make sure __eq__ returns True for identical HTMLNode instances.
    def test_eq(self):
        node1 = HTMLNode("a", "the Google web site", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("a", "the Google web site", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1, node2)
    
    # Purpose: Make sure __eq__ correctly returns False for HTMLNode instances.
    def test_eq_different_values(self):
        node1 = HTMLNode("a", "text1", None, {"href": "url1"})
        node2 = HTMLNode("a", "text2", None, {"href": "url1"})
        self.assertNotEqual(node1, node2)

    # Purpose: Make sure an exception is raised when the props type is specified as anything else than a 'dict' (or None)
    def test_props_type_invalid(self):
        with self.assertRaises(TypeError):
            node = HTMLNode("a", "text", None, ["not", "a", "dict"])
            node.props_to_html()

    # Purpose: Make sure the output of props_to_html is as expected
    def test_props_to_html_valid_dict(self):
        node = HTMLNode("a", "text", None, {"href": "https://example.com", "target": "_blank"})
        expected = 'href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)
    
    # Purpose: Make sure the output of __repr__ is as expected
    def test_repr_output(self):
        node = HTMLNode("p", "Hello", None, {"class": "intro"})
        output = repr(node)
        self.assertIn("Tag: p", output)
        self.assertIn("Value: Hello", output)
        self.assertIn("Props: {'class':", output)

    # Purpose: Make sure that defaults are applied correctly
    def test_arguments_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    