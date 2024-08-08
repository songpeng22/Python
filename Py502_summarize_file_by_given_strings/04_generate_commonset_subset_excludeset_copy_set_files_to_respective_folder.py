# -*- coding: utf-8 -*-
# @Time    : 2024/07/26
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : 04_generate_commonset_subset_excludeset_copy_set_files_to_respective_folder.py
# @Desc    : 计算集合，拷贝图片
#          ：找出目标集合和difficult集合的交集，然后把交集内容作为subset，目标集-subset=excludeset
#          ：最终将图片copy到各个集合的文件夹中

import os
import shutil

# 两个文件夹的交集
def find_common_files(dir_of_set01, dir_of_set02):
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

# 两个文件夹的差集（非集）
def find_missing_files(dir_of_set01, dir_of_set02):
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

def copy_files_to_target_dir(files, dir_of_target):
    folder = os.path.exists(dir_of_target)
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(dir_of_target)            #makedirs 创建文件时如果路径不存在会创建这个路径
        print("create dir " + dir_of_target)
    else:
        print("{dir_of_target} exist")
    for file in files:
        shutil.copy2(file, dir_of_target)

# defines
root_dir = 'E:\\PaddleOCR_Data\\'
dot_font_dir_name = 'train_data_00_dot_font'
steel_stamp_dir_name = 'train_data_00_steel_stamp'
target_dir_name = steel_stamp_dir_name
difficult_dif_name = 'train_data_00_difficult'

dir_of_mainset = root_dir + target_dir_name + '\\'
dir_of_subset = root_dir + target_dir_name + '_subset\\'
dir_of_excludeset = root_dir + target_dir_name + '_excludeset'

dir_of_difficult = root_dir + difficult_dif_name + '\\'

#
common_set = find_common_files(dir_of_mainset,dir_of_difficult)
for line in common_set:
    print(line)
copy_files_to_target_dir(common_set,dir_of_subset)
excludeset = find_missing_files(dir_of_mainset,dir_of_subset)
for line in excludeset:
    print(line)
copy_files_to_target_dir(excludeset,dir_of_excludeset)