from textnode import TextNode, TextType
#upgrade later for nested elements

def split_nodes_delimiter(old_nodes :list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        print(split_text)
        if len(split_text) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_text[i], text_type))
    return new_nodes