# -*- coding: utf-8 -*-
# @Time    : 2024/07/26
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : 03_summarize.py
# @Desc    : 统计数量
#          ：统计总集的数量，subset的数量，excludeset的数量

import os

def count_image_files(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png']
    count = 0

    for root, dirs, files in os.walk(folder_path):
        if root == folder_path:  # 确保只处理主目录，不处理子目录
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    count += 1

    return count

dir_of_mainset = 'E:\\PaddleOCR_Data\\train_data\\'
dir_of_subset = 'E:\\PaddleOCR_Data\\train_data_00_difficult\\'
dir_of_excludeset = 'E:\\PaddleOCR_Data\\train_data_00_main\\'

image_count = count_image_files(dir_of_mainset)
print(f'在文件夹 {dir_of_mainset} 中找到 {image_count} 张图片。')
image_count = count_image_files(dir_of_subset)
print(f'在文件夹 {dir_of_subset} 中找到 {image_count} 张图片。')
image_count = count_image_files(dir_of_excludeset)
print(f'在文件夹 {dir_of_excludeset} 中找到 {image_count} 张图片。')