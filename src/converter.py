from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

class Converter():
    @staticmethod
    def text_node_to_html_node(text_node: TextNode):
        if not isinstance(text_node.text_type, TextType):
            raise TypeError("'text_type' must be an instance of a TextType enum")
        if (text_node.text_type == TextType.LINK or text_node.text_type == TextType.IMAGE) and url == None:
            raise ValueError("'url' cannot be None when text type equals 'link' or 'image'")
        
        if text_node.text_type == TextType.TEXT:
            tag = None
        else:
            tag = text_node.text_type.value

        value = text_node.text
        return LeafNode(tag, value)

    @staticmethod
    def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
        new_nodes = []
        
        for node in old_nodes:
            if node.text == "":
                pass
            elif node.text_type is not TextType.TEXT:
                new_nodes.append(node)
            else:
                text_list = node.text.split(delimiter)
                if len(text_list) % 2 == 0:
                    # the list is an even number of items, so an unclosed md element was found
                    raise Exception("Unclosed markdown element found")
                else:
                    for i in range(len(text_list)):
                        if text_list[i] != "":    
                            if i % 2 == 0: # even      
                                new_node = TextNode(text_list[i] , TextType.TEXT)
                            else:
                                new_node = TextNode(text_list[i], text_type)
                        else:
                            continue
                        new_nodes.append(new_node)

        return new_nodes

def test_split():
    text_nodes = [TextNode("**bold text** normal text", TextType.TEXT),
                  TextNode("normal text **bold text** normal text", TextType.TEXT),
                  TextNode("normal text **bold text** normal text", TextType.TEXT),
                  TextNode("normal text **bold text**", TextType.TEXT)]
    
    converter = Converter()
    converted = converter.split_nodes_delimiter(text_nodes, "**", TextType.BOLD)

    for i in range(len(converted)):
        print(converted[i])
        

def main():
    test_split()
    
main()
