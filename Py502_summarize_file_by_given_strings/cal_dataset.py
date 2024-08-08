# -*- coding: utf-8 -*-
# @Time    : 2024/07/26
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : 05_main.py
# @Desc    : 计算集合
#          ：

import os
import shutil

# 单个文件的所有行，构成一个集合
def read_file_lines(file_path,is_sorted=False):
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

# 单个文件夹根目录的所有图片，构成一个集合(absolute path)
def find_file_paths(dir_of_set01):
    set01_files = set()
    image_extensions = ['.jpg', '.jpeg', '.png']

    # 遍历dir_of_mainset文件夹，获取所有文件的绝对路径
    for root, dirs, files in os.walk(dir_of_set01):
        if root == dir_of_set01:  # 确保只处理主目录，不处理子目录
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    relative_path = os.path.relpath(os.path.join(root, file), dir_of_set01)
                    set01_files.add(relative_path)

    # sort by names
    relative_paths = set01_files
    sorted_relative_paths = sorted(relative_paths, key=str.casefold)

    # 将差集中的文件的相对路径转换为绝对路径
    absolute_paths = [os.path.join(dir_of_set01, path) for path in sorted_relative_paths]

    return list(absolute_paths)

# 单个文件夹根目录的所有图片，构成一个集合(relative path)
def find_file_names(dir_of_set01):
    set01_files = set()
    image_extensions = ['.jpg', '.jpeg', '.png']
    # 遍历dir_of_subset文件夹，获取所有文件的绝对路径
    for root, dirs, files in os.walk(dir_of_set01):
        if root == dir_of_set01:  # 确保只处理主目录，不处理子目录
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    relative_path = os.path.relpath(os.path.join(root, file), dir_of_set01)
                    set01_files.add(file)
    return set01_files

# 两个文件夹根目录的所有图片，构成一个合集(absolute path)
def find_total_file_paths(dir_of_set01, dir_of_set02):
    set01_files = set()
    set02_files = set()
    image_extensions = ['.jpg', '.jpeg', '.png']

    # 遍历dir_of_mainset文件夹，获取所有文件的绝对路径
    for root, dirs, files in os.walk(dir_of_set01):
        if root == dir_of_set01:  # 确保只处理主目录，不处理子目录
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    set01_files.add(os.path.join(root, file))

    # 遍历dir_of_subset文件夹，获取所有文件的绝对路径
    for root, dirs, files in os.walk(dir_of_set02):
        if root == dir_of_set02:  # 确保只处理主目录，不处理子目录
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    set02_files.add(os.path.join(root, file))

    # 计算合集，得到两个文件夹都有的文件的绝对路径
    absolute_paths = list(set01_files | set02_files)
    sorted_absolute_paths = sorted(absolute_paths, key=str.casefold)

    return list(sorted_absolute_paths)

# 两个文件夹根目录共有图片，构成一个交集(absolute path)
def find_common_file_paths(dir_of_set01, dir_of_set02):
    set01_files = set()
    set02_files = set()
    image_extensions = ['.jpg', '.jpeg', '.png']

    # 遍历dir_of_mainset文件夹，获取所有文件的绝对路径
    for root, dirs, files in os.walk(dir_of_set01):
        if root == dir_of_set01:  # 确保只处理主目录，不处理子目录
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    relative_path = os.path.relpath(os.path.join(root, file), dir_of_set01)
                    set01_files.add(relative_path)

    # 遍历dir_of_subset文件夹，获取所有文件的绝对路径
    for root, dirs, files in os.walk(dir_of_set02):
        if root == dir_of_set02:  # 确保只处理主目录，不处理子目录
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    relative_path = os.path.relpath(os.path.join(root, file), dir_of_set02)
                    set02_files.add(relative_path)

    # 计算交集，得到两个文件夹都有的文件的绝对路径
    common_relative_paths = list(set01_files & set02_files)
    sorted_common_relative_paths = sorted(common_relative_paths, key=str.casefold)

    # 将差集中的文件的相对路径转换为绝对路径
    common_absolute_paths = [os.path.join(dir_of_set01, path) for path in sorted_common_relative_paths]

    return list(common_absolute_paths)

# 两个文件夹根目录图片，计算差集(absolute path)
def find_missing_file_paths(dir_of_set01, dir_of_set02):
    set01_files = set()
    set02_files = set()
    image_extensions = ['.jpg', '.jpeg', '.png']

    # 遍历dir_of_mainset文件夹，获取所有文件的绝对路径
    for root, dirs, files in os.walk(dir_of_set01):
        if root == dir_of_set01:  # 确保只处理主目录，不处理子目录
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    relative_path = os.path.relpath(os.path.join(root, file), dir_of_set01)
                    set01_files.add(relative_path)
    # print relative paths
    """
    print(f"print relative paths:")
    for element in set01_files:
        print(element)
    print(f"end of print relative paths")
    """

    # 遍历dir_of_subset文件夹，获取所有文件的绝对路径
    for root, dirs, files in os.walk(dir_of_set02):
        if root == dir_of_set02:  # 确保只处理主目录，不处理子目录
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    relative_path = os.path.relpath(os.path.join(root, file), dir_of_set02)
                    set02_files.add(relative_path)

    # 计算交集，得到两个文件夹都有的文件的绝对路径
    missing_relative_paths = set01_files - set02_files
    sorted_missing_relative_paths = sorted(missing_relative_paths, key=str.casefold)

    # 将差集中的文件的相对路径转换为绝对路径
    missing_absolute_paths = [os.path.join(dir_of_set01, path) for path in sorted_missing_relative_paths]

    return list(missing_absolute_paths)

# 两个集合，将第一个集合作为关键字keys，从第二个集合的lines中过滤filter，filter出含有keys的lines
def filter_lines_with_keys(lines,keys):
    bFoundAll = True
    lines_subset = set()
    lines_excluded = lines[:]
    countOfFound = 0
    countOfMainSet = len(lines)

    for key in keys:
        #print(key)
        bFound = False
        for line in lines:
            if line.find(key) != -1:
                #print(line)
                lines_excluded.remove(line)
                lines_subset.add(line)
                bFound = True
                countOfFound += 1
                break
        if(bFound != True):
            print(key + " not found!!!")
            bFoundAll = False

    sorted_lines_subset = sorted(lines_subset, key=str.casefold)
    sorted_lines_excluded = sorted(lines_excluded[:], key=str.casefold)

    print(f"mainset count:{countOfMainSet},found:{countOfFound},exclude count:{countOfMainSet - countOfFound}")
    #return (lines_subset,lines_excluded)
    return (sorted_lines_subset,sorted_lines_excluded)

dir_of_set01 = 'E:\\PaddleOCR_Data\\train_data_01_easy_test'
dir_of_set02 = 'E:\\PaddleOCR_Data\\train_data_01_easy_test_01_hmean1.0'
dir_of_set03 = 'E:\\PaddleOCR_Data\\train_data'
dir_of_set04 = 'E:\\PaddleOCR_Data\\train_data_00_difficult'
if __name__ == '__main__':
    dataset = find_file_paths(dir_of_set01)
    """
    print(f"print relative paths:")
    for element in dataset:
        print(element)
    print(f"end of print relative paths")
    """

    dataset = find_total_file_paths(dir_of_set01,dir_of_set02)

    dataset = find_common_file_paths(dir_of_set03,dir_of_set04)

    dataset = find_missing_file_paths(dir_of_set03,dir_of_set04)
    print(f"print relative paths:")
    for element in dataset:
        print(element)
    print(f"end of print relative paths")    