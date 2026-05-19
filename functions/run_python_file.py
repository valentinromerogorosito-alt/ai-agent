import subprocess
from google import genai
from google.genai import types
from .check_path_get_target import check_path_get_target


def run_python_file(working_directory, file_path, args=None):
    try:
        target_path = check_path_get_target(working_directory, file_path, "r")
        command = ["python", target_path]
        if args is not None:
            command.extend(args)
        subprocess_completed = subprocess.run(
            command,
            cwd=working_directory, 
            capture_output=True, 
            text=True, 
            timeout=30
        )
        output = ""
        if subprocess_completed.returncode != 0:
            output = f"Process exited with code {subprocess_completed.returncode}"

        if subprocess_completed.stdout == "" and subprocess_completed.stderr == "":
            output += "No output produced"
        if subprocess_completed.stdout != "":
            output += f"\nSTDOUT: {subprocess_completed.stdout}"
        if subprocess_completed.stderr != "":
            output += f"\nSTDERR: {subprocess_completed.stderr}"
        return output

    except subprocess.TimeoutExpired:
        return f"Error: subprocess 30 seconds execution time expired"
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes / runs a Python file in a specified path relative to the working directory with the optional arguments that are passed",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING, 
                description="File path to the file that is going to be run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY, 
                description="Arguments that specified file must be run with",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)
