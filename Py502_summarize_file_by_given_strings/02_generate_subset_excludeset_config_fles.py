# -*- coding: utf-8 -*-
# @Time    : 2024/07/26
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : 02_generate_subset_excludeset_config_fles.py
# @Desc    : 计算几何，拆分配置文件
#          ：根据subset文件夹中已有的图片，从总集中筛出三个配置文件对应的line
#          : 三个文件：Cache.cach fileState.txt Label.txt

import os
from cal_dataset import find_file_names
from cal_dataset import read_file_lines
from cal_dataset import filter_lines_with_keys
from utils import replace_string_in_file
from utils import write_lines_to_file

# 从文件夹的图片和三个配置文件，筛出difficult子集的三个配置文件
# 从总集和difficult子集，筛出非difficult子集
"""
def list_file(src_dir):
    files = os.listdir(file_dir)
    print('list files:')
    print(files)
    return files
files = list_file(file_dir)

# write file lists to file
file_path = "E:\\PaddleOCR_Data\\train_data_00_difficult\\filelists.txt"
filelist_path_of_mainset = dir_of_mainset + "filelists.txt"
filelist_path_of_subset = dir_of_subset + "filelists.txt"
filelist_path_of_excludeset = dir_of_excludeset + "filelists.txt"
def generate_file_path_list_file(tar_file):
    print('\nwrite file lists to file:')
    file = open(tar_file, "w") 
    for f in files:
        if f.endswith(".png"):
            print(f)
            file.write(f + "\n")
        elif f.endswith(".jpg"):
            print(f)
            file.write(f + "\n")
        elif f.endswith(".jpeg"):
            print(f)
            file.write(f + "\n")
        else:
            extension = f.split('.')
            #print(extension)
            #print(extension[-1] + "is excluded.")
            print(f + " is excluded.")
    file.close()
generate_file_path_list_file(file_path)
"""
# read file line by line
"""
#file_path = "E:\\PaddleOCR_Data\\train_data_00_difficult\\filelists.txt"
def read_file_line_by_line_with_strip(file_path):
    print('\nread file line by line:')
    # write lines to array
    lines_key = []
    with open(file_path, "r", encoding="utf-8") as file_in:
        for line in file_in:
            print(line.strip())
            lines_key.append(line.strip())
    return lines_key
#lines_keys = read_file_line_by_line_with_strip(filelist_path_of_subset)
"""

# write lines to array
#file_path_of_mainset = dir_of_mainset + target_file
"""
def read_file_line_by_line(file_path,is_sorted=False):
    print('\nread file line by line:')
    lines_full = []
    lines_return = []
    with open(file_path, "r", encoding="utf-8") as file_full:
        for line_full in file_full:
            #print(line_full)
            lines_full.append(line_full)
    if is_sorted:
        lines_return = sorted(lines_full, key=str.casefold)
    else:
        lines_return = lines_full[:]
    return lines_return
#lines_full = read_file_line_by_line(file_path_of_mainset)
"""

# generate file list from a dir
"""
def find_files_of_dir(dir):
    set01_files = set()
    image_extensions = ['.jpg', '.jpeg', '.png']
    # 遍历dir_of_subset文件夹，获取所有文件的绝对路径
    for root, dirs, files in os.walk(dir):
        if root == dir:  # 确保只处理主目录，不处理子目录
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    relative_path = os.path.relpath(os.path.join(root, file), dir)
                    set01_files.add(file)
    return set01_files
"""
# found keys is contained in Label.txt, and write into new path
#file_path_of_subset = dir_of_subset + target_file
#file_path_of_excludeset = dir_of_excludeset + target_file
"""
def filter_lines_with_keys(dir_of_subset,lines_file,file_new,generate_excludeset=False):
    bFoundAll = True
    countOfFound = 0
    #lines_keys = read_file_line_by_line_with_strip(keys_file)
    lines_keys = find_file_names(dir_of_subset)
    lines_full = read_file_lines(lines_file,True)
    lines_subset = set()
    lines_excluded = lines_full[:]
    countOfMainSet = len(lines_full)

    for key in lines_keys:
        #print(key)
        bFound = False
        for line in lines_excluded[:]:
            if line.find(key) != -1:
                #print(line)
                lines_excluded.remove(line)
                lines_subset.add(line)
                bFound = True
                countOfFound+=1
                break
        if(bFound != True):
            print(key + " not found!!!")
            bFoundAll = False

    with open(file_new, "w", encoding="utf-8") as _file_new:
        sorted_lines_subset = sorted(lines_subset, key=str.casefold)
        for line in sorted_lines_subset:
            _file_new.write(line)
    
    # generate excludeset file
    if(generate_excludeset):
        lines_excluded = sorted(lines_excluded[:], key=str.casefold)
        with open(file_path_of_excludeset, "w", encoding="utf-8") as _file_new:
            for line in lines_excluded:
                _file_new.write(line)
                
    print(f"main set count:{countOfMainSet},found:{countOfFound},exclude count:{countOfMainSet - countOfFound}")
    return bFoundAll
"""

def filter_lines_with_keys_ex(lines_keys,lines_full,file_new,generate_excludeset=False):
    lines_subset,lines_excluded = filter_lines_with_keys(lines_full,lines_keys)
    """
    with open(file_new, "w", encoding="utf-8") as _file_new:
        sorted_lines_subset = sorted(lines_subset, key=str.casefold)
        for line in sorted_lines_subset:
            _file_new.write(line)

    # generate excludeset file
    if(generate_excludeset):
        lines_excluded = sorted(lines_excluded[:], key=str.casefold)
        with open(file_path_of_excludeset, "w", encoding="utf-8") as _file_new:
            for line in lines_excluded:
                _file_new.write(line)            
    """
    write_lines_to_file(lines_subset,file_new)
    if(generate_excludeset):
        write_lines_to_file(lines_excluded,file_path_of_excludeset)


# defines
filter_src = ["Cache.cach","fileState.txt","Label.txt"]
root_dir = 'E:\\PaddleOCR_Data\\'
# element dir name
dir_name_of_train_data = 'train_data'
dir_name_of_difficult = 'train_data_00_difficult'
dir_name_of_main = 'train_data_00_main'
dir_name_of_dot_font = 'train_data_00_dot_font'
dir_name_of_steel_stamp = 'train_data_00_steel_stamp'
dir_name_of_Codystar = 'train_data_00_dot_font_Codystar'
dir_name_of_easy_test = 'train_data_01_easy_test'
dir_name_of_easy_test_codystar = 'train_data_01_easy_test_02_Codystar'
dir_name_of_easy_test_03 = 'train_data_01_easy_test_03'
dir_name_of_dot_font_horizontal = 'train_data_00_dot_font_horizontal'
# subset
dir_name_of_mainset = dir_name_of_train_data
dir_name_of_subset = dir_name_of_dot_font_horizontal # + '_subset'
dir_name_of_excludeset = dir_name_of_easy_test_03 # + '_excludeset'
# dir
dir_of_mainset = root_dir + dir_name_of_mainset + '\\'
dir_of_subset = root_dir + dir_name_of_subset + '\\'
dir_of_excludeset = root_dir + dir_name_of_excludeset + '\\'
is_generate_excludeset = False
# generate "Cache.cach"
target_file = filter_src[0]
file_path_of_mainset = dir_of_mainset + target_file
file_path_of_subset = dir_of_subset + target_file
file_path_of_excludeset = dir_of_excludeset + target_file
#bFoundAll = filter_lines_with_keys(dir_of_subset,file_path_of_mainset,file_path_of_subset,is_generate_excludeset)
lines_keys = find_file_names(dir_of_subset)
lines_full = read_file_lines(file_path_of_mainset,True)
filter_lines_with_keys_ex(lines_keys,lines_full,file_path_of_subset,is_generate_excludeset)

# replace path string
replace_string_in_file(file_path_of_subset,dir_name_of_mainset,dir_name_of_subset)
if is_generate_excludeset:
    replace_string_in_file(file_path_of_excludeset,dir_name_of_mainset,dir_name_of_excludeset)

# generate "fileState.txt"
"""
"""
target_file = filter_src[1]
file_path_of_mainset = dir_of_mainset + target_file
file_path_of_subset = dir_of_subset + target_file
file_path_of_excludeset = dir_of_excludeset + target_file
#bFoundAll = filter_lines_with_keys(dir_of_subset,file_path_of_mainset,file_path_of_subset,is_generate_excludeset)
lines_keys = find_file_names(dir_of_subset)
lines_full = read_file_lines(file_path_of_mainset,True)
filter_lines_with_keys_ex(lines_keys,lines_full,file_path_of_subset,is_generate_excludeset)
# replace path string
replace_string_in_file(file_path_of_subset,dir_name_of_mainset,dir_name_of_subset)
if is_generate_excludeset:
    replace_string_in_file(file_path_of_excludeset,dir_name_of_mainset,dir_name_of_excludeset)

# generate "Label.txt"
target_file = filter_src[2]
file_path_of_mainset = dir_of_mainset + target_file
file_path_of_subset = dir_of_subset + target_file
file_path_of_excludeset = dir_of_excludeset + target_file
#bFoundAll = filter_lines_with_keys(dir_of_subset,file_path_of_mainset,file_path_of_subset,is_generate_excludeset)
lines_keys = find_file_names(dir_of_subset)
lines_full = read_file_lines(file_path_of_mainset,True)
filter_lines_with_keys_ex(lines_keys,lines_full,file_path_of_subset,is_generate_excludeset)
# replace path string
replace_string_in_file(file_path_of_subset,dir_name_of_mainset,dir_name_of_subset)
if is_generate_excludeset:
    replace_string_in_file(file_path_of_excludeset,dir_name_of_mainset,dir_name_of_excludeset)
