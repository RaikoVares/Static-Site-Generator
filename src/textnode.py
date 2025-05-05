from enum import Enum 
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text 
        self.text_type = text_type
        self.url = url 

 
    def __eq__(self, obj):
        return (self.text == obj.text 
                and self.text_type == obj.text_type
                and self.url == obj.url) 
            

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    _type = text_node.text_type
    text = text_node.text
    if _type == TextType.TEXT:
        return LeafNode(None, text)
    elif _type == TextType.BOLD:
        return LeafNode("b", text)
    elif _type == TextType.ITALIC:
        return LeafNode("i", text)
    elif _type == TextType.CODE:
        return LeafNode("code", text)
    elif _type == TextType.LINK:
        return LeafNode("a", text, {"href":text_node.url})
    elif _type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url,
                                    "alt": text})
    else:
        raise ValueError("No type")

        
