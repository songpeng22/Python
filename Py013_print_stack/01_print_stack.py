# -*- coding: utf-8 -*-
# @Time    : 2024/08/09
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py013_print_stack\01_print_stack.py
# @Desc    : print stack to console and to logger file

import traceback
import inspect
import logging

# print stack to console
def print_stack():
    #traceback.print_stack()
    print(inspect.stack())

# log stack to logger file
def log_stack_trace(logger):
    stack = inspect.stack()
    logger.debug("Stack trace:")
    for frame in stack:
        frame_info = inspect.getframeinfo(frame[0])
        logger.debug(f"File: {frame_info.filename}, Line: {frame_info.lineno}, Function: {frame_info.function}")

# 配置 logging
logging.basicConfig(filename='C:\\Users\\songp\\Desktop\\test\\stack_trace.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    print( "main()" )
    # method 01 - traceback.print_stack()
    # method 02 - inspect.stack()
    #print_stack()
    # method 03 - output stack to logger file
    log_stack_trace(logging)