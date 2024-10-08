# -*- coding: utf-8 -*-
# @Time    : 2024/07/26
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : 05_data_migration.py
# @Desc    : data migration

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
from business import data_merge

dir_of_set01 = 'E:\\PaddleOCR_Data\\train_data_01_easy_test\\'
dir_of_set02 = 'E:\\PaddleOCR_Data\\train_data_01_easy_test_01_hmean1.0\\'
dir_of_set03 = 'E:\\PaddleOCR_Data\\train_data\\'
dir_of_set04 = 'E:\\PaddleOCR_Data\\train_data_00_difficult\\'
dir_of_set05 = 'E:\\PaddleOCR_Data\\train_data_00_dot_font_Codystar\\'
dir_of_set06 = 'E:\\PaddleOCR_Data\\train_data_01_easy_test_02_Codystar\\'
dir_of_set07 = 'E:\\PaddleOCR_Data\\train_data_01_easy_test_03\\'
dir_of_set08 = 'E:\\PaddleOCR_Data\\train_data_01_easy_test_05_Collect_018\\'
dir_of_set09 = 'E:\\PaddleOCR_Data\\train_data_01_easy_test_07_food503\\'
dir_of_set10 = 'E:\\PaddleOCR_Data\\train_data_02_merge_01_Collect_018_food503\\'
dir_of_target = dir_of_set10
if __name__ == '__main__':
    data_merge(dir_of_target,dir_of_set08,dir_of_set09)
