from pathlib import Path
import os

current_dir = Path('/')
available_operations = ['help', 'pwd', 'ls', 'cd', 'touch', 'cat', 'rm']


while True:
    operation = input(f'{Path.absolute(current_dir)}$ ').split(' ')
    if operation[0] in available_operations:
        if operation[0] == 'help':
            print('----AVAILABLE OPERATIONS---- \n\npwd - print the path of the current working directory \nls - list the files in the current directory \ncd (dir_name) - change the current working directory \ntouch (file_name) - creating a blanck new file \nrm (file_name) - remove the file \ncat (file_name) - print the file content\n')
            
        elif operation[0] == 'pwd':
            print(f"\n{Path.absolute(current_dir)}\n")
            
        elif operation[0] == 'ls':
            try:
                print(f"\n{os.listdir(current_dir)}\n")
            except FileNotFoundError:
                print('\nNo such file or directory\n')
                
        elif operation[0] == 'cd':
            if operation[1] == '..':
                current_dir = current_dir.parent
            else:
                current_dir = current_dir / operation[1]
                
        elif operation[0] == 'touch':
            with open(current_dir / operation[1], 'w') as f:
                f.write('')
                
        elif operation[0] == 'rm':
            try:
                file_name = operation[1]
                os.remove(current_dir / operation[1])
            except:
                print(f"\nCannot remove {operation[1]}: No such file in directory\n")
            
        elif operation[0] == 'cat':
            try:
                with open(current_dir / operation[1], 'r') as f:
                    for line in f:
                        print(line, end='\n')
            except:
                print(f"\nCannot open {operation[1]}: No such file in directory\n")
    else:
        print(f'\nInvalid operation {operation[0]}\n')