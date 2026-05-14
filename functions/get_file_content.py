import os
from .check_path_get_target import check_path_get_target
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try: 
       target_file = check_path_get_target(working_directory, file_path, "c")

        with open(target_file, "r") as f: 
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string

    except FileNotFoundError:
        return f'Error: Could not find file at {file_path}'
    except Exception as e:
        return f'Error: get_file_content({working_directory}, {file_path}) did not work as expected: {e}'

