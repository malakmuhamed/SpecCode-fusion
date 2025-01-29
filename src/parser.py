import ast
import os

def find_python_files_in_folder(folder):
    """Find all .py files in the specified folder."""
    python_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

def extract_functions(file_path):
    """Extract function names from a Python source code file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            tree = ast.parse(file.read())
        # Extract function names from the AST
        return [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

def extract_functions_from_content(content):
    """Extract function names from Python source code content."""
    try:
        tree = ast.parse(content)
        return [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    except Exception as e:
        print(f"Error parsing content: {e}")
        return []
