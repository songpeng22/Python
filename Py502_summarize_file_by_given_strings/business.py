# -*- coding: utf-8 -*-
# @Time    : 2024/07/26
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : business.py
# @Desc    : 业务逻辑
#          ：

import os
import shutil
from cal_dataset import find_file_paths
from cal_dataset import find_file_names
from cal_dataset import filter_lines_with_keys
from cal_dataset import read_file_lines
from utils import copy_files_to_target_dir
from utils import write_lines_to_file
from utils import replace_string_in_file
from utils import merge_config_files

# data migration
def data_migration(dir_src,dir_tar):
    # bitmap files
    dataset = find_file_paths(dir_src)
    copy_files_to_target_dir(dataset,dir_tar)
    # config files
    filter_src = ["Cache.cach","fileState.txt","Label.txt"]
    basename_of_src = os.path.basename(os.path.normpath(dir_src))
    basename_of_tar = os.path.basename(os.path.normpath(dir_tar))
    #print(f"basename_of_src:{basename_of_src},basename_of_tar:{basename_of_tar}")
    for element in filter_src:
        config_file = element
        file_path_of_src = dir_src + config_file
        file_path_of_target = dir_tar + config_file
        lines_keys = find_file_names(dir_tar)
        lines_full = read_file_lines(file_path_of_src,True)
        lines_subset,lines_excluded = filter_lines_with_keys(lines_full,lines_keys)
        write_lines_to_file(lines_subset,file_path_of_target)
        replace_string_in_file(file_path_of_target,basename_of_src,basename_of_tar)

# data merge
def data_merge(dir_tar,*dir_srcs):
    # check
    if not dir_tar.endswith('/') and not dir_tar.endswith("\\"):
        dir_tar += os.sep
    # copy files from srcs seperately
    for dir_src in dir_srcs:
        #print(dir_src)
        # bitmap files
        dataset = find_file_paths(dir_src)
        copy_files_to_target_dir(dataset,dir_tar)

    # merge config files
    filter_src = ["Cache.cach","fileState.txt","Label.txt"]
    for element in filter_src:
        config_file = element
        file_path_of_target = dir_tar + config_file
        file_path_of_srcs = []
        for dir_src in dir_srcs:
            file_path_of_src = dir_src + config_file
            file_path_of_srcs.append(file_path_of_src)
        merge_config_files(file_path_of_target,*file_path_of_srcs)


    
    