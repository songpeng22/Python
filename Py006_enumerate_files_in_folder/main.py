import os
"""
"""


files = os.listdir('E:\\PaddleOCR_Data\\train_data_04_capture\\')
print('list files:')
print(files)
print('\nlist files in lines:')
for file in files:
    print(file)


"""
"""
folder_path = "E:\\PaddleOCR_Data\\train_data_04_capture\\"

print('\nlist files of absolute path:')
for path, currentDirectory, files in os.walk(folder_path):
    for file in files:
        if not file.startswith("."):
            print(os.path.join(path, file))
