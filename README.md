# PYconverter: Jupyter Notebook (.ipynb) and Python Script (.py) Converter

**PYconverter** is a Python tool designed to simplify the conversion between Jupyter Notebook (`.ipynb`) files and Python script (`.py`) files. This tool allows users to easily convert their Jupyter notebooks into Python scripts for sharing or further development, and vice versa.

## Features

- **Convert Jupyter Notebooks to Python Scripts**: Seamlessly export all the code cells from a `.ipynb` file into a `.py` script.
- **Convert Python Scripts to Jupyter Notebooks**: Transform your Python scripts into Jupyter notebooks with the code contained in a single code cell.
- **User-Friendly Interface**: The tool provides a simple interface where users can choose their preferred conversion method and specify input/output file paths.

## How it Works

- The tool reads a Jupyter Notebook or Python file and converts it into the respective format based on the user's choice.
- It uses `nbconvert` to handle the export process for converting between the two formats.

### Usage Flow:
1. Choose the conversion type:
   - Convert from `.ipynb` to `.py`
   - Convert from `.py` to `.ipynb`
2. Provide the path of the input file and the desired output path for the converted file.
3. The converted file is saved at the specified location, and the process will notify you of successful conversion or any errors.

## Installation

To use **PYconverter**, you need to have the following libraries installed:

- `nbformat` – For working with Jupyter Notebook files.
- `nbconvert` – To export and convert between notebook and script formats.

You can install the required libraries by running:

```bash
pip install nbformat nbconvert
