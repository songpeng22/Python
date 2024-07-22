import os
"""
"""

dir = 'E:\\PaddleOCR_Data\\train_data_00_difficult\\'
files = os.listdir(dir)
print('list files:')
print(files)
print('\nlist files in lines:')
for file in files:
    print(file)

# list files of absolute path:
print('\nlist files of absolute path:')
import pathlib
for filepath in pathlib.Path(dir).glob('**/*'):
    print(filepath.absolute())

"""
"""
# list files of absolute path:
print('\nlist files of absolute path:')
for path, currentDirectory, files in os.walk(dir):
    for file in files:
        if not file.startswith("."):
            print(os.path.join(path, file))

