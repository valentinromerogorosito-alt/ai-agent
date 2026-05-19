import os


def check_path_get_target(working_directory, current_path, option):
    options = {"i": "list", "c": "read", "w": "write to", "r": "execute"}
    try: 
        working_dir_abs = os.path.abspath(working_directory)
        target = os.path.normpath(os.path.join(working_dir_abs, current_path))
        
        valid_path = os.path.commonpath([working_dir_abs, target]) == working_dir_abs
        if not valid_path:
            return f'Error: Cannot {options[option]} "{current_path}" as it is outside the permitted working directory'
        
        # get_files_info
        if option == "i": 
            if not os.path.isdir(target):
                return f'Error: "{current_path}" is not a directory'
            return target

        # get_file_contents
        if option == "c":
            if not os.path.isfile(target):
                return f'Error: File not found or is not a regular file: "{current_path}"'
            return target 

        # write_file
        if option == "w":
            if os.path.isdir(target):
                return f'Error: Cannot write to "{current_path}" as it is a directory'
            # Create nested directories if they don't exist
            os.makedirs(current_path, exist_ok=True)
            return target 

        # run_python_file
        if option == "r":
            if not os.path.isfile(target):
                return f'Error: "{current_path}" does not exist or is not a regular file'
            if not target.endswith(".py"): 
                return f'Error: "{current_path}" is not a Python file'
            return target 



    except FileNotFoundError:
        return f'Error: Could not find file at {current_path}'
    except Exception as e:
        return f'Error: check_path_get_target({working_directory}, {current_path}, {option}) did not work as expected:\n  {e}'

