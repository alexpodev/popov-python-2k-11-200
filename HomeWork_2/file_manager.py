from pathlib import Path
import os

current_dir = Path('/')
available_operations = ['pwd']

while True:
    operation = input(f'{Path.absolute(current_dir)}$ ')
    if any(map(operation.__contains__, available_operations)):
        if operation == 'pwd':
            print(f"\n{Path.absolute(current_dir)}\n")
            
    else:
        print(f'\nInvalid operation {operation}\n')