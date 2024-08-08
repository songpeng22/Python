# -*- coding: utf-8 -*-
# @Time    : 2024/07/26
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : 06_test.py
# @Desc    : test

import os
import shutil
import sys
"""
# import module - solution 01
sys.path.append(os.getcwd())
import cal_dataset 
cal_dataset.find_files(dir_of_set01)
"""
# import module - solution 02
"""
from cal_dataset import find_files
dataset = find_files(dir_of_set01)
"""
from cal_dataset import find_file_paths
from cal_dataset import find_file_names
from cal_dataset import filter_lines_with_keys
from utils import copy_files_to_target_dir
from business import data_merge


dir_of_set01 = 'E:\\PaddleOCR_Data\\train_data_01_easy_test'
dir_of_set02 = 'E:\\PaddleOCR_Data\\train_data_01_easy_test_01_hmean1.0'
dir_of_set03 = 'E:\\PaddleOCR_Data\\train_data'
dir_of_set04 = 'E:\\PaddleOCR_Data\\train_data_00_difficult'
dir_of_set05 = 'E:\\PaddleOCR_Data\\train_data_00_dot_font_Codystar'
dir_of_set06 = 'E:\\PaddleOCR_Data\\train_data_01_easy_test_02_Codystar'
dir_of_set07 = 'E:\\PaddleOCR_Data\\train_data_01_easy_test_03'
if __name__ == '__main__':
    """
    dataset = find_file_paths(dir_of_set01)
    print(f"print relative paths:")
    for element in dataset:
        print(element)
    print(f"end of print relative paths")

    copy_files_to_target_dir(dataset,dir_of_set05)
    """
    """
    dataset = find_file_names(dir_of_set01)
    print(f"print relative paths:")
    for element in dataset:
        print(element)
    print(f"end of print relative paths")
    """
    
    data_merge(dir_of_set07,dir_of_set02,dir_of_set06)


    
    


