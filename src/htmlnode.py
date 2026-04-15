class HTMLNode(tag = None, value = None, children = None, props = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

    def to_html(self):
        raise NotImplementedError("Child classes will override this method to render themselves as HTML")

    def props_to_html(self):
        result =""
        if self.props is None:
            return ""
        for key in self.props:
            result += " " + key + "=" + '"' + self.props[key] + '"'
        return result

    def __repr__(self):
        return f"HTMLNODE({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.value is None:
            raise ValueError("Value braucht Wert")
        if self.tag is None:
            return str(self.value)   
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):    
        super().__init__(tag, None, children, props)   
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag braucht Wert")
        if self.children is None:
            raise ValueError("Children braucht Wert")
        result = ""
        for i in self.children:
            result += i.to_html()
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"

        



