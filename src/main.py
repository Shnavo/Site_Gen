import os
import shutil
import sys

from directory_manipulation import clear_copy
from page_creators import generate_page_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template = "./template.html"


def main():

    basepath = "/"
    if len(sys.argv) < 1:
        basepath = sys.argv[1]
 

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    clear_copy(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page_recursive(dir_path_content, template, dir_path_public, basepath)

# print(sys.argv[1])

main()
