import os
from .check_path_get_target import check_path_get_target


def get_files_info(working_directory, directory="."):
    target_dir = check_path_get_target(working_directory, directory, "i") 

    try:
        target_dir_contents_info = get_directory_contents_info(target_dir)
        directory_print_contents_info(target_dir_contents_info)
    except Exception as e:
        return f"Error when trying to extract and print content's info from taget directory: {e}"

    return None

def get_directory_contents_info(directory):
    directory_contents_info = {}
    for file_name in os.listdir(directory):
        # Check for os normalize possible requirement
        file_path = os.path.join(directory, file_name)
        file_info = {
            "file_size": os.path.getsize(file_path), 
            "is_dir": os.path.isdir(file_path)
        }
        directory_contents_info[file_name] = file_info 
    return directory_contents_info

def directory_print_contents_info(directory_contents_info):
    for content in directory_contents_info:
        content_dict = directory_contents_info[content]
        print(f"  - {content}: file_size={content_dict['file_size']} bytes, is_dir={content_dict['is_dir']}")
