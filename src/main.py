import os
import shutil

from directory_manipulation import clear_copy
from page_creators import generate_page_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template = "./template.html"



def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    clear_copy(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page_recursive(dir_path_content, template, dir_path_public)


main()
