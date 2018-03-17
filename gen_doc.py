import os
from info import *

def gen_code_contents(filename):
    contents = ['```python\n\n']
    with open(filename, 'r') as code_file:
        contents.append(code_file.read())
    contents.append('```\n\n')
    return contents

def gather_code_contents():
    filename_list = os.listdir()
    contents = []
    contents.append('## Examples\n\n')
    for filename in filename_list:
        if '.py' in filename:
            name = filename.split('.')[0].split('_')
            if name[0] == 'example':
                example_name = ' '.join(term for term in name[1:])
                contents.append('### ' + example_name + '\n\n')
                code_contents = gen_code_contents(filename)
                contents.extend(code_contents)
    return contents

def output_readme(contents):
    output_string = ''.join(content for content in contents)
    with open('docs/README.md', 'w') as doc_file:
        doc_file.write(output_string)
    with open('README.md', 'w') as readme_file:
        readme_file.write(output_string)

def gen_intro():
    contents = []
    contents.append('# ' + PROJECT_NAME + '\n\n')
    contents.append('version: ' + PROJECT_VERSION + '\n\n')
    contents.append(PROJECT_DESCRIPTION + '\n\n')
    return contents

def main():
    contents = []
    contents.extend(gen_intro())
    contents.extend(gather_code_contents())
    output_readme(contents)

if __name__ == '__main__':
    main()
