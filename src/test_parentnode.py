# Purpose: Make sure two instances of the ParentNode class are the same.
import unittest
from src.htmlnode import HTMLNode, LeafNode, ParentNode

# Valid equality
def test_eq_different_values(self):
    children = [
        LeafNode("li", "This is a list item"),
        LeafNode("li", "This is another list item"),
        LeafNode("li", "And another list item"),
    ]
    node1 = ParentNode("ul", children, None)
    node2 = ParentNode("ul", children, None)
    self.assertEqual(node1, node2)

# Expected HTML output
def test_to_html_output(self):
    children = [
        LeafNode("li", "This is a list item"),
        LeafNode("li", "This is another list item"),
        LeafNode("li", "And another list item"),
    ]
    node1 = ParentNode("ul", children)
    expected = "<ul><li>This is a list item</li><li>This is another list item</li><li>And another list item</li></ul>"
    self.assertIn(node1.to_html(), expected)

# repr falls back to to_html
def test_repr_matches_to_html(self):
    children = [LeafNode("li", "Item")]
    node = ParentNode("ul", children)
    self.assertEqual(repr(node), node.to_html())

# # Invalid child type
# def test_invalid_child_type_raises():
#     with pytest.raises(TypeError):
#         ParentNode("ul", ["not_a_node"])

# # Invalid tag for a ParentNode
# def test_invalid_tag_for_parentnode_raises():
#     children = [LeafNode("li", "Item")]
#     with pytest.raises(ValueError):
#         ParentNode("em", children)  # 'em' is inline

# # Valid structure but invalid child tag
# def test_invalid_child_tag_for_ul_raises():
#     children = [LeafNode("div", "Not allowed in <ul>")]
#     with pytest.raises(ValueError):
#         ParentNode("ul", children)

# # Props are rendered properly
# def test_props_are_rendered_correctly():
#     children = [LeafNode("li", "Item")]
#     node = ParentNode("ul", children, props={"class": "list", "id": "main-list"})
#     html = node.to_html()
#     assert html.startswith('<ul class="list" id="main-list">')
#     assert html.endswith("</ul>")

# # Empty children list
# def test_empty_children_renders_properly():
#     node = ParentNode("div", [])
#     assert node.to_html() == "<div></div>"

# # None props are safe
# def test_none_props_renders_cleanly():
#     children = [LeafNode("li", "Item")]
#     node = ParentNode("ul", children, props=None)
#     assert node.to_html().startswith("<ul>")
