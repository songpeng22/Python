import os
from utils import replace_string_in_file

file_path_of_set01 = 'E:\\PaddleOCR_Data\\train_data_00_dot_font_horizontal\\val.txt'
file_path_of_set02 = 'E:\\PaddleOCR_Data\\train_data_01_easy_test_01_hmean1.0\\val.txt'
if __name__ == '__main__':
    # transfer label.txt to val.txt(absolute path)
    replace_string_in_file(file_path_of_set02,"train_data_01_easy_test_01_hmean1.0/","E:\\PaddleOCR_Data\\train_data_01_easy_test_01_hmean1.0\\")
