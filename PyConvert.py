# Import the nbformat library for working with Jupyter Notebook (.ipynb) files
import nbformat

# Importing PythonExporter and ScriptExporter for exporting the notebook as Python code
from nbconvert import PythonExporter, ScriptExporter

# Import the os library to handle file paths
import os

# Function to convert a Jupyter Notebook (.ipynb) to a Python script (.py)
def convert_ipynb_to_py(input_path, output_path):
    """
    Converts a Jupyter Notebook (.ipynb) file to a Python (.py) file.

    :param input_path: Path to the input .ipynb file
    :param output_path: Path to save the converted .py file
    """
    try:
        # Open the .ipynb file and read its content using nbformat
        with open(input_path, 'r', encoding='utf-8') as file:
            notebook_content = nbformat.read(file, as_version=4)  # Read the notebook in version 4 format

        # Create an instance of PythonExporter to export the notebook content as Python code
        python_exporter = PythonExporter()

        # Convert the notebook's content to Python code
        python_code, _ = python_exporter.from_notebook_node(notebook_content)

        # Write the converted Python code to a new .py file
        with open(output_path, 'w', encoding='utf-8') as py_file:
            py_file.write(python_code)

        # Inform the user that the conversion was successful
        print(f"Conversion successful: '{input_path}' -> '{output_path}'")

    except Exception as e:
        # Catch any errors during the conversion process and display them
        print(f"Error during conversion: {e}")

# Function to convert a Python script (.py) to a Jupyter Notebook (.ipynb)
def convert_py_to_ipynb(input_path, output_path):
    """
    Converts a Python (.py) file to a Jupyter Notebook (.ipynb) file.

    :param input_path: Path to the input .py file
    :param output_path: Path to save the converted .ipynb file
    """
    try:
        # Open the Python (.py) file and read its content
        with open(input_path, 'r', encoding='utf-8') as file:
            python_code = file.read()  # Read the Python code from the .py file

        # Create a new Jupyter notebook object (notebook node)
        notebook_node = nbformat.v4.new_notebook()

        # Add the Python code as a new code cell to the notebook
        notebook_node.cells.append(nbformat.v4.new_code_cell(python_code))

        # Write the newly created notebook to a .ipynb file
        with open(output_path, 'w', encoding='utf-8') as ipynb_file:
            nbformat.write(notebook_node, ipynb_file)

        # Inform the user that the conversion was successful
        print(f"Conversion successful: '{input_path}' -> '{output_path}'")

    except Exception as e:
        # Catch any errors during the conversion process and display them
        print(f"Error during conversion: {e}")

# Main function to prompt the user for the conversion choice and file paths
def main():
    """
    Main function to prompt the user for conversion options and handle file conversions.
    """
    # Prompt the user to choose the type of conversion they want to perform
    print("What do you want to convert?")
    print("1. .ipynb to .py")
    print("2. .py to .ipynb")
    choice = input("Enter your choice (1 or 2): ").strip()

    # If the user chooses to convert from .ipynb to .py
    if choice == '1':
        input_path = input("Enter the path of the .ipynb file: ").strip()  # Get the path to the .ipynb file
        output_path = input("Enter the path to save the .py file: ").strip()  # Get the path to save the .py file
        convert_ipynb_to_py(input_path, output_path)  # Call the conversion function
    
    # If the user chooses to convert from .py to .ipynb
    elif choice == '2':
        input_path = input("Enter the path of the .py file: ").strip()  # Get the path to the .py file
        output_path = input("Enter the path to save the .ipynb file: ").strip()  # Get the path to save the .ipynb file
        convert_py_to_ipynb(input_path, output_path)  # Call the conversion function
    
    # If the user enters an invalid choice
    else:
        print("Invalid choice. Please enter 1 or 2.")  # Prompt the user to enter a valid choice

# This ensures the main function runs when the script is executed directly
if __name__ == "__main__":
    main()
