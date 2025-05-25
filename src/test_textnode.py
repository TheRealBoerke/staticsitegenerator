import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a bold text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_wrong_arguments(self):
        node = TextNode("Hello", TextType.BOLD, url="https://boot.dev")
        node2 = TextNode("Hello", TextType.BOLD, url="https://boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is an italic text node", TextType.ITALIC)
        self.assertNotEqual(node,node2)

    def test_url_not_present_exception(self):
        # store the exception that will be thrown in the context variable
        with self.assertRaises(ValueError) as context:
            TextNode("This is a link text node, but the URL is missing", TextType.LINK)
        # check if the given string is in str(context.exception).
        self.assertIn("'url' cannot be None when text type equals 'link'", str(context.exception))
    
    def test_invalidtype_value_exception(self):
        with self.assertRaises(TypeError) as context:
            TextNode("This is a stupid mistake", "TextType.BOLD")
        # check if the given string is in str(context.exception).
        self.assertIn("'text_type' must be an instance of a TextType enum", str(context.exception))

if __name__ == "__main__":
    unittest.main()