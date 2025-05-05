
from textnode import TextType, TextNode, text_node_to_html_node




def main():
    
    node = TextNode("This is text with a `code` node", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)
    # html_node = text_node_to_html_node(node)
    # print(html_node)

if __name__ == "__main__":
    main()
