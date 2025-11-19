from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def block_to_block_type(block: str) -> BlockType:
    print(block)
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    split_block = block.split("\n")
    q = 0
    u = 0
    o = 0
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


def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
        if blocks[i] == "":
            blocks.remove(blocks[i])
    return blocks
