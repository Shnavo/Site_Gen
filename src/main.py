import os
import shutil

from directory_manipulation import clear_copy

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    clear_copy(dir_path_static, dir_path_public)


main()
