# -*- coding: utf-8 -*-
# @Time    : 2024/08/16
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py502_summarize_file_by_given_strings\07_replace_string.py
# @Desc    : 替换字符串

import os
from utils import replace_string_in_file

file_path_of_set01 = 'E:\\PaddleOCR_Data\\train_data_00_dot_font_horizontal\\val.txt'
file_path_of_set02 = 'E:\\PaddleOCR_Data\\train_data_01_easy_test_01_hmean1.0\\val.txt'
if __name__ == '__main__':
    # transfer label.txt to val.txt(absolute path)
    replace_string_in_file(file_path_of_set02,"train_data_01_easy_test_01_hmean1.0/","E:\\PaddleOCR_Data\\train_data_01_easy_test_01_hmean1.0\\")
