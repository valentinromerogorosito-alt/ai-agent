import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try: 
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        valid_file_path = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file, "r") as f: 
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string

    except FileNotFoundError:
        return f'Error: Could not find file at {file_path}'
    except Exception as e:
        return f'Error: get_file_content({working_directory}, {file_path}) did not work as expected: {e}'

