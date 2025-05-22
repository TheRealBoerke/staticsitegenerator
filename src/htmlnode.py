class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        # Initially I entered Dictionary, but since it's a Python 
        if self.props is not None and not isinstance(self.props, dict):
            raise TypeError("'props' should be of type 'dict' or None")
        if self.props != None:
            output = ""
            for key, value in self.props.items():
                output += f"{key}=\"{value}\" "
            return output.strip()
        else:
            return ""

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

    def __repr__(self):
        output = f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props_to_html()}"
        return output
