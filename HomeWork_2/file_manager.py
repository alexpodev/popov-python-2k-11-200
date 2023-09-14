from pathlib import Path
import os

current_dir = Path('/')
available_operations = ['help', 'pwd', 'ls', 'cd', 'touch', 'cat', 'rm']

while True:
    operation = input(f'{Path.absolute(current_dir)}$ ')
    if any(map(operation.__contains__, available_operations)):
        if operation == 'pwd':
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
    else:
        print(f'\nInvalid operation {operation}\n')