# React Project Structure and Content Generator

This Python script generates a comprehensive Markdown document that captures both the structure of your React project and the content of its component files. It's designed to provide a quick and easy way to share your project's layout and code with Large Language Models (LLMs) or other developers, facilitating faster understanding and more effective communication about your project.

## Purpose

When working with LLMs or collaborating with other developers, it's often beneficial to provide a clear overview of your project structure along with the actual code content. This script automates the process of gathering this information, saving you time and ensuring consistency in your documentation.

## Features

- Generates a tree-like structure of your React project
- Excludes non-essential directories like `node_modules`, `.git`, etc.
- Captures the content of React component files (`.js`, `.jsx`, `.ts`, `.tsx`) and stylesheets (`.css`)
- Ignores test files and other non-component files
- Outputs everything into a single, well-formatted Markdown file

## How to Use

1. Place the `generate_project_doc.py` script in the root directory of your React project.
2. Run the script using Python:
   ```
   python generate_project_doc.py
   ```
3. Find the generated `project_structure_and_content.md` file in the same directory.

## Output

The generated Markdown file will contain:

1. A section showing the overall project structure
2. A section with the content of each component file, numbered and formatted in code blocks

