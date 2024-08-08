# -*- coding: utf-8 -*-
# @Time    : 2024/07/26
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : copy_files.py
# @Desc    : 文件拷贝
#          ：

import os
import shutil

# 从文件集合(abosolute path)，逐个拷贝文件到目标目录
def copy_files_to_target_dir(files_set, dir_of_target):
    folder = os.path.exists(dir_of_target)
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(dir_of_target)            #makedirs 创建文件时如果路径不存在会创建这个路径
        print("create dir " + dir_of_target)
    else:
        print("{dir_of_target} exist")
    for file in files_set:
        shutil.copy2(file, dir_of_target)

# replace string in file
def replace_string_in_file(file_path,old_string,new_string):
    print(f"file:{file_path}, replace {old_string} with {new_string}")
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    # 替换字符串
    new_content = file_content.replace(old_string, new_string)

    # 将修改后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

# write lines to file
def write_lines_to_file(lines,file):
    with open(file, "w", encoding="utf-8") as _file:
        sorted_lines_subset = sorted(lines, key=str.casefold)
        for line in sorted_lines_subset:
            _file.write(line)

# merge files
def merge_config_files(output_file, *input_files):
    """
    Merges multiple text files into a single file, removing empty lines.

    Args:
        output_file (str): The path to the output file.
        *input_files (str): The paths to the input text files.
    """
    print(f"open output_file:{output_file}")
    with open(output_file, 'w', encoding='utf-8') as output_f:
        for input_file in input_files:
            print(f"open input_file:{input_file}")
            with open(input_file, 'r', encoding='utf-8') as input_f:
                #content = input_f.read().strip()
                #if content:
                content = input_f.read()
                output_f.write(content)
                #output_f.write('\n\n')  # Add a separator between files

    print(f"Merged text files saved to: {output_file}")


