from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    text_node = TextNode("Boerke is the very greatest.", TextType.BOLD_TEXT)
    html_node = HTMLNode(None,None,None,{"href":"https://google.com","target": "_blank"})
    print(html_node)
main()