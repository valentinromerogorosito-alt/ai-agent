import os
from .check_path_get_target import check_path_get_target


def write_file(working_directory, file_path, content):
    target_file = check_path_get_target(working_directory, file_path, "w")
   
    try:
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: when trying to write to {file_path}:\n  {e}'
            

