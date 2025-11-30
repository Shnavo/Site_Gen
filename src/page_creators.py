from blocks import markdown_to_blocks, markdown_to_html_node
import os


def extract_title(markdown: str):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith(("#", "# ")) and not block.startswith("##"):
            header = block.lstrip("#").strip()
            return header
    raise Exception("site needs a header")


def generate_page(dir_path_content: str, template_path: str, dest_path: str, basepath: str):
    print(f"Generating page from {dir_path_content} to {dest_path} using {template_path}")
    with open(dir_path_content) as f:
        markdown = f.read()

    with open(template_path) as f:
        template = f.read()

    html = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    # if not os.path.exists(dest_dir_path):
    #     os.makedirs(dest_dir_path)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, mode="w") as f:
        f.write(template)


def generate_page_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str):
    for item in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item).replace(".md", ".html")
        if os.path.isdir(from_path):
            generate_page_recursive(from_path, template_path, dest_path, basepath)
            continue
        else:
            generate_page(from_path, template_path, dest_path, basepath)

