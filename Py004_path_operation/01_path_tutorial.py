# -*- coding: utf-8 -*-
# @Time    : 2024/08/21
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py004_path_operation\01_path_tutorial.py
# @Desc    : path tutorial

import os

# current file path
print(f"current file path")
absolute_file_path = os.path.abspath(__file__)
print(f"current file path: {absolute_file_path}")

# current file name
current_file_name = os.path.basename(absolute_file_path)
print(f"current_file_name: {current_file_name}")

# absolute dir path
absolute_dir_path = os.path.dirname(absolute_file_path)
print(f"absolute_dir_path: {absolute_dir_path}")

# current dir name
current_dir_name = os.path.basename(absolute_dir_path)
print(f"current_dir_name: {current_dir_name}")
