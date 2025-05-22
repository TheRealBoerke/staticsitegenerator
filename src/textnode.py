from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "normal text"
    BOLD_TEXT = "bold text"
    ITALIC_TEXT = "italic text"
    CODE_TEXT = "code text"
    LINKS = "links"
    IMAGES = "images" 

class TextNode():
    def __init__(self, text, text_type, url=None):
        if not isinstance(text_type, TextType):
            raise TypeError("'text_type' must be an instance of a TextType enum")
        if (text_type == TextType.LINKS or text_type == TextType.IMAGES) and url == None:
            raise ValueError("'url' cannot be None when text type equals 'links' or 'images'")
            
        self.text = text
        self.text_type = text_type
        if not(text_type == TextType.LINKS or text_type == TextType.IMAGES) and url != None:
            self.url = None
        else:
            self.url = url
    
    def __eq__(self, other):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

