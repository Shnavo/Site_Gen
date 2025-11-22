from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import ParentNode, LeafNode
import re

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


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple]:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text: str) -> list[tuple]:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def text_to_text_nodes(text: str) -> list[TextNode]:
    node = TextNode(text, TextType.TEXT)
    finished = [node]
    finished = split_nodes_delimiter(finished, "**", TextType.BOLD)
    finished = split_nodes_delimiter(finished, "_", TextType.ITALIC)
    finished = split_nodes_delimiter(finished, "`", TextType.CODE)
    finished = split_nodes_image(finished)
    finished = split_nodes_link(finished)
    return finished

def text_to_children(text: str) -> list[LeafNode]:
    paragraph = newline_stripper(text)
    text_children = text_to_text_nodes(paragraph)
    html_children = []
    for child in text_children:
        html_children.append(text_node_to_html_node(child))
    return html_children

def newline_stripper(node: str) -> str:
    stripped = node.split("\n")
    node= " ".join(stripped)
    return node

def md_prefix_stripper(block: str):
    # if block.startswith("#"):
    return block.lstrip("# ")


def heading_counter(text: str):
    if text.startswith("# "):
        return "h1"
    if text.startswith("## "):
        return "h2"
    if text.startswith("### "):
        return "h3"
    if text.startswith("#### "):
        return "h4"
    if text.startswith("##### "):
        return "h5"
    if text.startswith("###### "):
        return "h6"
