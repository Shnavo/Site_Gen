def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
        if blocks[i] == "":
            blocks.remove(blocks[i])
    return blocks
