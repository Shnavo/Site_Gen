import shutil
import os


def clear_copy(
    source_dir_path: str,
    dest_dir_path: str,
):
    """
    Copies items from the static folder to the provided path

    :param dest_dir_path: Path of the location for the generated site based on the files provided in source_dir_path
    :param source_dir_path: Path of the location of the source files for the generated site
    :type dest_dir_path: str
    :type source_dir_path: str
    """
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for item in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, item)
        dest_path = os.path.join(dest_dir_path, item)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            clear_copy(from_path, dest_path)
