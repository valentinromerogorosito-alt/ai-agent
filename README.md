## Installation / setup 
### Create venv
uv venv

### Activate venv
source .venv/bin/activate

## Project Arquitecture
## ./functions
### ./functions/get_files_info.py
Guardrail for getting files info.

### ./functions/get_file_content.py
Guardrail for getting files content.

### ./functions/write_file.py
Guardrail for writing files.

### ./functions/check_path_get_target.py
Helper function that checks the validity of the file based of it exists, is on the working directory and . Gets the target file or directory path, configured depending on the function that call it. 

