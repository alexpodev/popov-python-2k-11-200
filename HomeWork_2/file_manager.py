from pathlib import Path
import os

current_dir = Path('/')
available_operations = ['help', 'pwd', 'ls', 'cd', 'touch', 'cat', 'rm']

while True:
    operation = input(f'{Path.absolute(current_dir)}$ ')
    if any(map(operation.__contains__, available_operations)):
        if operation == 'help':
            print('----AVAILABLE OPERATIONS---- \n\npwd - print the path of the current working directory \nls - list the files in the current directory \ncd (dir_name) - change the current working directory \ntouch (file_name) - creating a blanck new file \nrm (file_name) - remove the file \ncat (file_name) - print the file content\n')
            
        elif operation == 'pwd':
            print(f"\n{Path.absolute(current_dir)}\n")
            
        elif operation == 'ls':
            try:
                print(f"\n{os.listdir(current_dir)}\n")
            except FileNotFoundError:
                print('\nNo such file or directory\n')
                
        elif operation.startswith('cd '):
            if operation[3:] == '..':
                current_dir = current_dir.parent
            else:
                current_dir = current_dir / operation[3:]
                
        elif operation.startswith('touch '):
            file_name = operation[6:]
            with open(current_dir / file_name, 'w') as f:
                f.write('')
                
        elif operation.startswith('rm '):
            try:
                file_name = operation[3:]
                os.remove(current_dir / file_name)
            except:
                print(f"\nCannot remove {file_name}: No such file in directory\n")
            
        elif operation.startswith('cat '):
            file_name = operation[4:]
            try:
                with open(current_dir / file_name, 'r') as f:
                    for line in f:
                        print(line, end='\n')
            except:
                print(f"\nCannot open {file_name}: No such file in directory\n")
    else:
        print(f'\nInvalid operation {operation}\n')