# -*- coding: utf-8 -*-
# @Time    : 2024/07/26
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : 01_copy_excludeset_to_excludeset_folder.py
# @Desc    : logger in a file

import logging
from datetime import datetime

logger_initialized = {}
logger_name = "mylogger"
def get_logger(name=logger_name, log_level=logging.DEBUG):
    """Initialize and get a logger by name.
    If the logger has not been initialized, this method will initialize the
    logger by adding one or two handlers, otherwise the initialized logger will
    be directly returned. During initialization, a StreamHandler will always be
    added. If `log_file` is specified a FileHandler will also be added.
    Args:
        name (str): Logger name.
        log_file (str | None): The log filename. If specified, a FileHandler
            will be added to the logger.
        log_level (int): The logger level. Note that only the process of
            rank 0 is affected, and other processes will set the level to
            "Error" thus be silent most of the time.
    Returns:
        logging.Logger: The expected logger.
    """    
    # 创建一个logger对象
    logger = logging.getLogger(name)
    if name in logger_initialized:
        print(f"logger already exist, return exist one")
        return logger
    for logger_name in logger_initialized:
        if name.startswith(logger_name):
            print(f"logger already exist, return exist one")
            return logger
    
    logger.setLevel(log_level)

    # 获取当前时间并格式化为字符串
    #current_time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')[:-3]
    current_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    # 生成输出文件路径
    output_dir = 'C:\\Users\\songp\\Desktop\\test\\'
    output_file_path = output_dir + current_time + ".txt"
    # 创建file handler
    file_handler = logging.FileHandler(output_file_path)
    file_handler.setLevel(log_level)

    # 创建stream handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger_initialized[name] = True

    return logger

def reinit_logger(name=logger_name):
    print(f"reinit_logger()")
    logger_initialized.clear()