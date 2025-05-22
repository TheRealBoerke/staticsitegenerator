import unittest
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    # Purpose: Make sure __eq__ returns True for identical LeafNode instances.
    def test_eq(self):
        node1 = LeafNode("a", "the Google web site", {"href": "https://www.google.com", "target": "_blank"})
        node2 = LeafNode("a", "the Google web site", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1, node2)
    
    # Purpose: Make sure __eq__ correctly returns False for LeafNode instances.
    def test_eq_different_values(self):
        node1 = LeafNode("a", "text1", {"href": "url1"})
        node2 = LeafNode("a", "text2", {"href": "url1"})
        self.assertNotEqual(node1, node2)

    # Purpose: Make sure an exception is raised when the props type is specified as anything else than a 'dict' (or None)
    def test_props_type_invalid(self):
        with self.assertRaises(TypeError):
            node = LeafNode("a", "text", None, ["not", "a", "dict"])
            node.props_to_html()

    # Purpose: Make sure the output of props_to_html is as expected
    def test_props_to_html_valid_dict(self):
        node = LeafNode("a", "text", {"href": "https://example.com", "target": "_blank"})
        expected = 'href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    # Purpose: Make sure an empty string is returned when props equals to None
    def test_props_to_html_none(self):
        node = LeafNode("a", "text", None)
        self.assertEqual(node.props_to_html(), "")

    # Purpose: Make sure the to_html() result is as expected
    def test_leaf_to_html_p(self):
        node1 = LeafNode("p", "Hello, world!")
        node2 = LeafNode("a", "Google", {"href": "https://www.google.com"})
        self.assertEqual(node1.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Google</a>')
    
    # Purpose: Make sure the output of __repr__ is as expected
    def test_repr_output(self):
        node = LeafNode("p", "Hello", {"class": "intro"})
        output = repr(node)
        self.assertEqual('<p class="intro">Hello</p>', output)

    # Purpose: Make sure that arguments are of the correct type
    def test_tag_wrong_type(self):
        with self.assertRaises(TypeError):
            LeafNode(123,"Value",None) # 'tag' should be a string

    def test_tag_wrong_type(self):
        with self.assertRaises(TypeError):
            LeafNode("div",123,None) # 'value' should be a string
    
    def test_props_wrong_type(self):
        with self.assertRaises(TypeError):
            LeafNode("p","Hello world","HEY! This is not a dict") # 'props' must be a dict or None

if __name__ == "__main__":
    unittest.main()