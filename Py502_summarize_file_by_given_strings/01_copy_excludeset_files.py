import os
import shutil

# defines
dir_of_subset = 'E:\\PaddleOCR_Data\\train_data_00_difficult\\'
dir_of_mainset = 'E:\\PaddleOCR_Data\\train_data\\'
dir_of_excludeset = 'E:\\PaddleOCR_Data\\train_data_00_main\\'
filelist_path_of_subset = "E:\\PaddleOCR_Data\\train_data_00_difficult\\filelists.txt"
filelist_path_of_mainset = "E:\\PaddleOCR_Data\\train_data\\filelists.txt"
filelist_path_of_excludeset = "E:\\PaddleOCR_Data\\train_data_00_main\\filelists.txt"
filelist_absolute_path_of_subset = "E:\\PaddleOCR_Data\\train_data_00_difficult\\filelists_absolute.txt"
filelist_absolute_path_of_mainset = "E:\\PaddleOCR_Data\\train_data\\filelists_absolute.txt"
filelist_absolute_path_of_excludeset = "E:\\PaddleOCR_Data\\train_data_00_main\\filelists_absolute.txt"

# generage list of files(only include jpg jpeg png)
def generate_files_array(src_dir):
    files = os.listdir(src_dir)
    print('list files:')
    print(files)
    print('\nwrite file lists to file:')
    files_with_exts = []
    for f in files:
        if f.endswith(".png"):
            print(f)
            files_with_exts.append(f)
        elif f.endswith(".jpg"):
            print(f)
            files_with_exts.append(f)
        elif f.endswith(".jpeg"):
            print(f)
            files_with_exts.append(f)
        else:
            extension = f.split('.')
            #print(extension)
            #print(extension[-1] + "is excluded.")
            print(f + " is excluded.")
    print(files_with_exts)
    return files_with_exts

# generage list of abosolut paths(only include jpg jpeg png)
def generate_file_absolute_paths(src_dir):
    # generate absolute path list
    absolute_paths = []
    image_extensions = ['.jpg', '.jpeg', '.png']
    for _path, _currentDirectory, _files in os.walk(src_dir):
        for _file in _files:
            if any(_file.lower().endswith(ext) for ext in image_extensions):
                file_path = os.path.join(_path, _file)
                absolute_paths.append(file_path)
    print(absolute_paths)
    return absolute_paths

def find_missing_files(dir_of_subset, dir_of_mainset):
    mainset_files = set()
    subset_files = set()
    image_extensions = ['.jpg', '.jpeg', '.png']

    # 遍历dir_of_mainset文件夹，获取所有文件的绝对路径
    for root, dirs, files in os.walk(dir_of_mainset):
        if root == dir_of_mainset:  # 确保只处理主目录，不处理子目录
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    relative_path = os.path.relpath(os.path.join(root, file), dir_of_mainset)
                    mainset_files.add(relative_path)

    # 遍历dir_of_subset文件夹，获取所有文件的绝对路径
    for root, dirs, files in os.walk(dir_of_subset):
        if root == dir_of_subset:  # 确保只处理主目录，不处理子目录
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    relative_path = os.path.relpath(os.path.join(root, file), dir_of_subset)
                    subset_files.add(relative_path)
    print(subset_files)

    # 计算差集，得到只在dir_of_mainset中存在的文件
    missing_relative_paths = mainset_files - subset_files

    # 将差集中的文件的相对路径转换为绝对路径
    missing_absolute_paths = [os.path.join(dir_of_mainset, path) for path in missing_relative_paths]

    return list(missing_absolute_paths)

def copy_files_to_excludeset(missing_files, dir_of_excludeset):
    for file in missing_files:
        shutil.copy2(file, dir_of_excludeset)

#generate_files_array(dir_of_subset)
#generate_file_absolute_paths(dir_of_mainset)
#generate_file_absolute_paths(dir_of_subset)
missing_files = find_missing_files(dir_of_subset,dir_of_mainset)
copy_files_to_excludeset(missing_files, dir_of_excludeset)