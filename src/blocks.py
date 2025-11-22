from enum import Enum
from splitter import text_to_text_nodes
from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
        if blocks[i] == "":
            blocks.remove(blocks[i])
    return blocks


def block_to_block_type(block: str) -> BlockType:
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    split_block = block.split("\n")
    q = 0
    # quote counter
    u = 0
    # unordered list counter
    o = 0
    # ordered list counter
    for i in range(len(split_block)):
        if split_block[i].startswith(">"):
            q += 1
        if split_block[i].startswith("- "):
            u += 1
        if split_block[i].startswith(f"{i+1}. "):
            o += 1
    if q == len(split_block):
        return BlockType.QUOTE
    if u == len(split_block):
        return BlockType.UNORDERED_LIST
    if o == len(split_block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            children.append(paragraph_to_html_node(block))
        if block_type == BlockType.HEADING:
            children.append(heading_to_html_node(block))
        if block_type == BlockType.QUOTE:
            children.append(quote_to_html_node(block))
        if block_type == BlockType.UNORDERED_LIST:
            children.append(ulist_to_html_node(block))
        if block_type == BlockType.ORDERED_LIST:
            children.append(olist_to_html_node(block))
        if block_type == BlockType.CODE:
            children.append(code_to_htmml_node(block))
    return ParentNode("div", children)

def text_to_children(text: str) -> list[LeafNode]:
    text_children = text_to_text_nodes(text)
    html_children = []
    for child in text_children:
        html_children.append(text_node_to_html_node(child))
    return html_children

def paragraph_to_html_node(block: str) -> ParentNode:
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block: str) -> ParentNode:
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def quote_to_html_node(block: str) -> ParentNode:
    lines = block.split("\n")
    text_list = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        text_list.append(line.lstrip(">").strip())
    final_text = " ".join(text_list)
    children = text_to_children(final_text)
    return ParentNode("blockquote", children)

def ulist_to_html_node(block: str) -> ParentNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def olist_to_html_node(block: str) -> ParentNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def code_to_htmml_node(block: str) -> ParentNode:
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])