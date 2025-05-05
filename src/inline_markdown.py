
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    new_nodes = []

    for j, node in enumerate(old_nodes):
        print(node)
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        _lst = node.text.split(delimiter)    
        if len(_lst) % 2 == 0:
            raise ValueError("Invalid markdown syntax")
            

        _nodes = []
        for i, item in enumerate(_lst):
            if item == "":
                continue
            if i % 2 != 0:
                _nodes.append(TextNode(item, text_type))
            else:
                _nodes.append(TextNode(item, TextType.TEXT))
        new_nodes.extend(_nodes)

    return new_nodes
