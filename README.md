# Project Structure and Content Generators

This repository contains two Python scripts designed to generate comprehensive Markdown documents that capture both the structure of your projects and the content of their source files. These tools are created to provide a quick and easy way to share your project's layout and code with Large Language Models (LLMs) or other developers, facilitating faster understanding and more effective communication about your projects.

## Scripts

1. `react_generate_project_doc.py`: For React projects
2. `spring_boot_generate_project_doc.py`: For Spring Boot/Java projects

## Purpose

When working with LLMs or collaborating with other developers, it's often beneficial to provide a clear overview of your project structure along with the actual code content. These scripts automate the process of gathering this information, saving you time and ensuring consistency in your documentation.

## Features

### React Project Generator (`react_generate_project_doc.py`)

- Generates a tree-like structure of your React project
- Excludes non-essential directories like `node_modules`, `.git`, etc.
- Captures the content of React component files (`.js`, `.jsx`, `.ts`, `.tsx`) and stylesheets (`.css`)
- Ignores test files and other non-component files

### Spring Boot Project Generator (`spring_boot_generate_project_doc.py`)

- Generates a tree-like structure of your Spring Boot project
- Excludes non-essential directories like `.idea`, `.mvn`, `target`, `build`, etc.
- Excludes files like `HELP.md`, `mvnw`, and `mvnw.cmd`
- Captures the content of all Java files in the `src/main/java` directory

## How to Use

1. Place the appropriate script in the root directory of your project:
   - For React projects: `react_generate_project_doc.py`
   - For Spring Boot projects: `spring_boot_generate_project_doc.py`
2. Run the script using Python:
   ```
   python react_generate_project_doc.py
   ```
   or
   ```
   python spring_boot_generate_project_doc.py
   ```
3. Find the generated `project_structure_and_content.md` file in the same directory.

## Output

The generated Markdown file will contain:

1. A section showing the overall project structure
2. A section with the content of each relevant source file, numbered and formatted in code blocks

## Benefits

- Quickly generate up-to-date documentation of your project
- Easily share your project structure and code with LLMs for better context
- Facilitate code reviews and onboarding of new team members
- Maintain a snapshot of your project's current state
