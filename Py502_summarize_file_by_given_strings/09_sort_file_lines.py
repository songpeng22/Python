# -*- coding: utf-8 -*-
# @Time    : 2024/08/16
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py502_summarize_file_by_given_strings\09_sort_file_lines.py
# @Desc    : 把文件内容，按照名称排序

from cal_dataset import read_file_lines
from utils import write_lines_to_file

# root
root_dir = 'E:\\PaddleOCR_Data\\'
# dir name
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
dir_name_of_collect_018 = 'train_data_01_easy_test_05_Collect_018'
# dir
dir_of = root_dir + dir_name_of_collect_018 + '\\'
# file name
file_name_of_cache = 'Cache.cach'
file_name_of_label = 'Label.txt'
file_name_of_file_state = 'fileState.txt'
# file path
file_path_of_cache = dir_of + file_name_of_cache
file_path_of_label = dir_of + file_name_of_label
file_path_of_file_state = dir_of + file_name_of_file_state

if __name__ == '__main__':
    print(f"file_path_of_cache:{file_path_of_cache}")
    print(f"file_path_of_label:{file_path_of_label}")
    print(f"file_path_of_file_state:{file_path_of_file_state}")
    #read sort and write back
    lines_01 = read_file_lines(file_path_of_cache,True)
    write_lines_to_file(lines_01,file_path_of_cache + '.bak')
    lines_02 = read_file_lines(file_path_of_label,True)
    write_lines_to_file(lines_02,file_path_of_label + '.bak')
    lines_03 = read_file_lines(file_path_of_file_state,True)
    write_lines_to_file(lines_03,file_path_of_file_state + '.bak')
