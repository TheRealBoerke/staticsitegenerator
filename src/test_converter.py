import unittest
from converter import Converter
from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestConverter(unittest.TestCase):

    def test_text_node_to_html_node_text(self):
        node = TextNode("Hello", TextType.TEXT)
        html_node = Converter.text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "Hello")

    def test_text_node_to_html_node_bold(self):
        node = TextNode("bold", TextType.BOLD)
        html_node = Converter.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "bold")
        self.assertEqual(html_node.value, "bold")

    def test_text_node_to_html_node_italic(self):
        node = TextNode("italic", TextType.ITALIC)
        html_node = Converter.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "italic")
        self.assertEqual(html_node.value, "italic")

    def test_text_node_to_html_node_invalid_type(self):
        with self.assertRaises(TypeError):
            node = TextNode("fail", "not-a-texttype")
            Converter.text_node_to_html_node(node)

    def test_split_nodes_delimiter_basic(self):
        nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        result = Converter.split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual([(n.text, n.text_type) for n in result], [(n.text, n.text_type) for n in expected])

    def test_split_nodes_delimiter_multiple_delimiters(self):
        nodes = [TextNode("This is **bold** and **strong**", TextType.TEXT)]
        result = Converter.split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("strong", TextType.BOLD)
        ]
        self.assertEqual([(n.text, n.text_type) for n in result], [(n.text, n.text_type) for n in expected])
        
    def test_split_nodes_delimiter_multiple_nodes(self):
        nodes = [TextNode("This is **bold** and **strong**", TextType.TEXT), TextNode("", TextType.TEXT)]
        result = Converter.split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("strong", TextType.BOLD)
        ]
        self.assertEqual([(n.text, n.text_type) for n in result], [(n.text, n.text_type) for n in expected])

    def test_split_nodes_delimiter_ignores_non_text(self):
        nodes = [TextNode("test", TextType.ITALIC)]
        result = Converter.split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, nodes)

    def test_split_nodes_delimiter_empty_node(self):
        nodes = [TextNode("", TextType.TEXT)]
        result = Converter.split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, [])

    def test_split_nodes_delimiter_unclosed(self):
        nodes = [TextNode("Unclosed **bold", TextType.TEXT)]
        with self.assertRaises(Exception):
            Converter.split_nodes_delimiter(nodes, "**", TextType.BOLD)

if __name__ == '__main__':
    unittest.main()
