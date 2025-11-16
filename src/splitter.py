from textnode import TextNode, TextType
from extractor import extract_markdown_images, extract_markdown_links

# upgrade later for nested elements


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:

    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)
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


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        temp_nodes = []
        if node.text_type is not TextType.TEXT:
            temp_nodes.append(node)
            continue

        urls: list[tuple[str, ...]] = extract_markdown_images(node.text)
        split_text = node.text.split(f"![{urls[0][0]}]({urls[0][1]})", 1)
        text_to_split = []
        for i in range(len(urls)):
            text_to_split = split_text.pop(-1)
            split_text.extend(text_to_split.split(f"![{urls[i][0]}]({urls[i][1]})", 1))
        for i in range(len(split_text)):
            if split_text[i] == "":
                if len(urls) < i:
                    temp_nodes.append(TextNode(urls[i][0], TextType.IMAGE, urls[i][1]))
                continue
            temp_nodes.append(TextNode(split_text[i], TextType.TEXT))
            temp_nodes.append(TextNode(urls[i][0], TextType.IMAGE, urls[i][1]))

        if temp_nodes == []:
            for pair in urls:
                temp_nodes.append(TextNode(pair[0], TextType.IMAGE, pair[1]))

        new_nodes.extend(temp_nodes)
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        temp_nodes = []
        if node.text_type is not TextType.TEXT:
            temp_nodes.append(node)
            continue

        urls: list[tuple[str, ...]] = extract_markdown_images(node.text)
        split_text = node.text.split(f"[{urls[0][0]}]({urls[0][1]})", 1)
        text_to_split = []
        for i in range(len(urls)):
            text_to_split = split_text.pop(-1)
            split_text.extend(text_to_split.split(f"[{urls[i][0]}]({urls[i][1]})", 1))
        for i in range(len(split_text)):
            if split_text[i] == "":
                if len(urls) < i:
                    temp_nodes.append(TextNode(urls[i][0], TextType.LINK, urls[i][1]))
                continue
            temp_nodes.append(TextNode(split_text[i], TextType.TEXT))
            temp_nodes.append(TextNode(urls[i][0], TextType.LINK, urls[i][1]))

        if temp_nodes == []:
            for pair in urls:
                temp_nodes.append(TextNode(pair[0], TextType.LINK, pair[1]))

        new_nodes.extend(temp_nodes)

    return new_nodes
