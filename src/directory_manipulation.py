import shutil
import os


def clear_copy(
    src_path: str,
    dst_path: str,
):
    """
    Copies items from the static folder to the provided path

    :param dst_path: Path of the location for the generated site based on the files provided in src_path
    :param src_path: Path of the location of the source files for the generated site
    :type dst_path: str
    :type src_path: str
    """
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)

    for item in os.listdir(src_path):
        from_path = os.path.join(src_path, item)
        dest_path = os.path.join(dst_path, item)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:

            clear_copy(from_path, dest_path)
