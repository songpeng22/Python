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
from business import data_migration

dir_of_src = 'E:\\PaddleOCR_Data\\train_data_01_easy_test\\'
dir_of_tar = 'E:\\PaddleOCR_Data\\train_data_01_easy_test_01_hmean1.0\\'
if __name__ == '__main__':
    data_migration(dir_of_src,dir_of_tar)
