'''
Day 77: Automation script
Write a script to automate file renaming.
'''

import os

def rename_files(directory, prefix='', suffix='', extension=None):
    '''
    Renames all files in the given directory based on the provided prefix, suffix, and extension.
    
    Parameters:
    - directory: The folder where files are located.
    - prefix: Text to add at the beginning of the filename.
    - suffix: Text to add at the end of the filename.
    - extension: If provided, files will be renamed with this extension (e.g., '.txt'). If None, keeps original extension.
    '''

    files = os.listdir(directory)

    if not files:
        print(f"don't have any archive in this directory: {directory}")
        return
    
    for filename in files:
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            print(f"skip the directory: {filename}")
            continue

        base_name, ext = os.path.splitext(filename)

        new_name = prefix + base_name + suffix

        if extension:
            new_name = new_name + extension
        else:
            new_name = new_name + ext

        
        new_file_path = os.path.join(directory, new_name)

        
        
        try: 
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_name}")
        except Exception as e:
            print(f"Error ao renomear: {filename}: {e}")

directory = r'C:\Users\Ingryd\OneDrive\Área de Trabalho\Todo'
prefix = 'test'
suffix = '_automate'
extension = ".txt"

rename_files(directory, prefix, suffix, extension)