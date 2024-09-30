import nbformat
from nbconvert import PythonExporter, ScriptExporter
import os

def convert_ipynb_to_py(input_path, output_path):
    """
    Converts a Jupyter Notebook (.ipynb) file to a Python (.py) file.

    :param input_path: Path to the input .ipynb file
    :param output_path: Path to save the converted .py file
    """
    try:
        # For reading the .ipynb file
        with open(input_path, 'r', encoding='utf-8') as file:
            notebook_content = nbformat.read(file, as_version=4)

        # Creating an instance of PythonExporter
        python_exporter = PythonExporter()

        # To convert the notebook's content to Python code
        python_code, _ = python_exporter.from_notebook_node(notebook_content)

        # Writing the Python code to a .py file
        with open(output_path, 'w', encoding='utf-8') as py_file:
            py_file.write(python_code)

        print(f"Conversion successful: '{input_path}' -> '{output_path}'")

    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_py_to_ipynb(input_path, output_path):
    """
    Converts a Python (.py) file to a Jupyter Notebook (.ipynb) file.

    :param input_path: Path to the input .py file
    :param output_path: Path to save the converted .ipynb file
    """
    try:
        # For reading the Python(.py) file's content
        with open(input_path, 'r', encoding='utf-8') as file:
            python_code = file.read()

        # Creating a new notebook node
        notebook_node = nbformat.v4.new_notebook()
        notebook_node.cells.append(nbformat.v4.new_code_cell(python_code))

        # To write the notebook node to an .ipynb file
        with open(output_path, 'w', encoding='utf-8') as ipynb_file:
            nbformat.write(notebook_node, ipynb_file)

        print(f"Conversion successful: '{input_path}' -> '{output_path}'")

    except Exception as e:
        print(f"Error during conversion: {e}")

def main():
    """
    Main function to prompt the user for conversion options and handle file conversions.
    """
    print("What do you want to convert?")
    print("1. .ipynb to .py")
    print("2. .py to .ipynb")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        input_path = input("Enter the path of the .ipynb file: ").strip()
        output_path = input("Enter the path to save the .py file: ").strip()
        convert_ipynb_to_py(input_path, output_path)
    elif choice == '2':
        input_path = input("Enter the path of the .py file: ").strip()
        output_path = input("Enter the path to save the .ipynb file: ").strip()
        convert_py_to_ipynb(input_path, output_path)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
