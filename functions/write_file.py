import os
from google import genai
from google.genai import types
from .check_path_get_target import check_path_get_target


def write_file(working_directory, file_path, content=""):
    target_file = check_path_get_target(working_directory, file_path, "w")
   
    try:
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: when trying to write to {file_path}:\n  {e}'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes a file in a specified path relative to the working directory with the content being passed",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING, 
                description="File path to the file that is going to be written, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING, 
                description="Content the specified file must be written with",
            ),
        },
        required=["file_path", "content"],
    ),
)
