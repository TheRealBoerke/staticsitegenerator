class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        # Initially I entered Dictionary, but since it's a Python 
        if self.props is not None and not isinstance(self.props, dict):
            raise TypeError("'props' should be of type 'dict' or None")
        if self.props is not None:
            output = ""
            for key, value in self.props.items():
                output += f"{key}=\"{value}\" "
            return output.strip()
        else:
            return ""

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if (tag is None):
            pass
        elif (not isinstance(tag, str)):
            raise TypeError("'tag' must be a string")
        
        if not isinstance(value, str):
            raise TypeError("'value' must be a string")
        
        if props is not None and not isinstance(props, dict):
            raise TypeError("'props' must be a dict or None")       
        
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props
    
    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.props == other.props)

    def __repr__(self):
        return self.to_html()

    def to_html(self):
        if self.value is None:
            raise ValueError("'value' cannot be None")
        if self.tag is None or self.tag == "":
            return self.value
        else:
            tag_close = f"</{self.tag}>"

            if self.props is None:
                tag_open = f"<{self.tag}>"
            else:
                tag_open = f"<{self.tag} {self.props_to_html()}>"
            
            return f"{tag_open}{self.value}{tag_close}"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag = tag, children = children, props = props)
        if tag is not None or not isinstance(tag, str):
            raise TypeError("'tag' must be a string")
        if props is not None and not isinstance(props, dict):
            raise TypeError("'props' must be a dict or None")
        
    def __eq__(self, other):
        if not isinstance(other, ParentNode):
            return False
        return (self.tag == other.tag and
                self.children == other.children and
                self.props == other.props)
    
    def __repr__(self):
        return f"ParentNode({self.tag},{self.children},{self.properties})"

    def to_html(self):
        tag_close = f"</{self.tag}>"

        # Yes, I know this could be done in one line... But hey, I'm a n00b...
        props_string = self.props_to_html()
        if props_string:
            tag_open = f"<{self.tag} {props_string}>"
        else:
            tag_open = f"<{self.tag}>"

        child_nodes_html = "".join(child.to_html() for child in self.children)

        return f"{tag_open}{child_nodes_html}{tag_close}"