import os
import re

def generate_project_structure(root_dir):
    structure = []
    exclude = set(['.idea', '.mvn', 'target', 'build'])
    exclude_files = set(['HELP.md', 'mvnw', 'mvnw.cmd'])
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in exclude]
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        structure.append(f'{indent}{os.path.basename(root)}/')
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            if file not in exclude_files:
                structure.append(f'{sub_indent}{file}')
    return '\n'.join(structure)

def extract_java_content(root_dir):
    content = []
    file_count = 1
    src_main_java = os.path.join(root_dir, 'src', 'main', 'java')
    for root, dirs, files in os.walk(src_main_java):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                relative_path = os.path.relpath(file_path, src_main_java)
                content.append(f"### {file_count}. {relative_path}\n\n```java\n{file_content}\n```\n")
                file_count += 1
    return '\n'.join(content)

def main():
    root_dir = '.'  # Assuming the script is run from the project root
    output_file = 'project_structure_and_content.md'
    
    # Generate project structure
    structure = generate_project_structure(root_dir)
    
    # Extract Java content
    content = extract_java_content(root_dir)
    
    # Combine structure and content
    full_content = f"# Project Structure\n\n```\n{structure}\n```\n\n# Java Source Code\n\n{content}"
    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"Project structure and content have been saved to {output_file}")

if __name__ == "__main__":
    main()