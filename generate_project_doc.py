import os

def generate_project_structure(root_dir):
    structure = []
    exclude = set(['node_modules', '.git', '.vscode', 'build', 'public'])
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in exclude]
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        structure.append(f'{indent}{os.path.basename(root)}/')
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            if file not in ['.env', '.gitignore', 'package-lock.json', 'package.json']:
                structure.append(f'{sub_indent}{file}')
    return '\n'.join(structure)

def extract_component_content(root_dir):
    content = []
    file_count = 1
    for root, dirs, files in os.walk(os.path.join(root_dir, 'src', 'components')):
        for file in files:
            if file.endswith(('.js', '.jsx', '.ts', '.tsx', '.css')) and not file.endswith('.test.js'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                content.append(f"### {file_count}. {file}\n\n```{file.split('.')[-1]}\n{file_content}\n```\n")
                file_count += 1
    
    for file in ['App.js', 'App.css']:
        file_path = os.path.join(root_dir, 'src', file)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
            content.append(f"### {file_count}. {file}\n\n```{file.split('.')[-1]}\n{file_content}\n```\n")
            file_count += 1
    
    return '\n'.join(content)

def main():
    root_dir = '.'
    output_file = 'project_structure_and_content.md'
    
    structure = generate_project_structure(root_dir)
    content = extract_component_content(root_dir)
    full_content = f"# Project Structure\n\n```\n{structure}\n```\n\n# Component Content\n\n{content}"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"Project structure and content have been saved to {output_file}")

if __name__ == "__main__":
    main()