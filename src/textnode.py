from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image" 

class TextNode():
    def __init__(self, text, text_type, url=None):
        if not isinstance(text_type, TextType):
            raise TypeError("'text_type' must be an instance of a TextType enum")
        if (text_type == TextType.LINK or text_type == TextType.IMAGE) and url == None:
            raise ValueError("'url' cannot be None when text type equals 'link' or 'image'")

        self.text = text
        self.text_type = text_type
        if not(text_type == TextType.LINK or text_type == TextType.IMAGE) and url != None:
            self.url = None
        else:
            self.url = url
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

