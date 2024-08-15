import os
import sys
import time
import inspect
#from ppocr.utils.logging import get_logger
from collections import deque
from logger import get_logger
logger = get_logger()

# solution 01 - 上次路径与本次相同，不再重复输出
is_solution_01 = False
last_printed_file = None
last_printed_file_name = None

# solution 02 - 记录下路径，同样路径不再重复输出
is_solution_02 = False
printed_files = {}

# solution 03 - 短时间内，不再重复输出
is_solution_03 = False
# 设置阈值（毫秒）
last_print_time = {}
output_threshold_ms = 500  # n毫秒内不重复输出

# solution 04 - 最近五次输出过，不再重复输出
# 这个方法可以缩短检索列表的长度，避免由于检索的列表过长，出现大量短时间重入的情况
is_solution_04 = False
recent_calls = deque(maxlen = 6)  # 存储最近n次调用的文件路径

def clean_old_entries():
    current_time_ms = time.time() * 1000  # 当前时间（毫秒）
    # 清理超过一定时间未更新的条目
    for file in list(last_print_time.keys()):
        if (current_time_ms - last_print_time[file]) > output_threshold_ms * 2:  # n倍阈值
            del last_print_time[file]
            del printed_files[file]

# 每个文件都检查 - 排除了stack里的冗余数据 - <frozen...>等
def trace_calls_01(frame, event, arg):
    global logger

    if event == 'call':
        # 跳过冻结的模块 - 这个方法虽然能提前得知文件名，但是该来的冗余信息还是会来
        if frame.f_code.co_filename.startswith('<frozen'):
            return

        current_file = frame.f_code.co_filename
        current_file_name = os.path.basename(frame.f_code.co_filename)
        function_name = frame.f_code.co_name
        line_no = frame.f_lineno

        print(f"caller:{current_file_name},func:{function_name},line:{line_no}")
        """
            
        logger = get_logger()
        logger.debug(f"caller: {current_file}")
        """

    return trace_calls_01

# 对连续的相同的路径，进行过滤
def trace_calls_02(frame, event, arg):
    global logger
    global last_printed_file_name

    if event == 'call':
        # 跳过冻结的模块 - 这个方法虽然能提前得知文件名，但是该来的冗余信息还是会来
        if frame.f_code.co_filename.startswith('<frozen'):
            return

        current_file = frame.f_code.co_filename
        current_file_name = os.path.basename(frame.f_code.co_filename)
        function_name = frame.f_code.co_name
        line_no = frame.f_lineno

        if current_file_name != last_printed_file_name:
            last_printed_file_name = current_file_name

            print(f"caller:{current_file_name},func:{function_name},line:{line_no}")
            """
                
            logger = get_logger()
            logger.debug(f"caller: {current_file}")
            """            

    return trace_calls_02

# 对队列中，最近出现过的路径/文件，进行过滤
def trace_calls_03(frame, event, arg):
    global logger
    global recent_calls

    if event == 'call':
        # 跳过冻结的模块 - 这个方法虽然能提前得知文件名，但是该来的冗余信息还是会来
        if frame.f_code.co_filename.startswith('<frozen'):
            return

        current_file = frame.f_code.co_filename
        current_file_name = os.path.basename(frame.f_code.co_filename)
        function_name = frame.f_code.co_name
        line_no = frame.f_lineno

        if current_file_name not in recent_calls:
            recent_calls.append(current_file_name)  # 添加到最近调用列表

            print(f"caller:{current_file_name},func:{function_name},line:{line_no}")
            """
                
            logger = get_logger()
            logger.debug(f"caller: {current_file}")
            """   

    return trace_calls_03

# 对最近一段时间出现过频繁的路径/文件，进行过滤
def trace_calls_04(frame, event, arg):
    global logger
    global last_printed_file
    global printed_files
    global last_print_time

    if event == 'call':
        # 跳过冻结的模块 - 这个方法虽然能提前得知文件名，但是该来的冗余信息还是会来
        if frame.f_code.co_filename.startswith('<frozen'):
            return

        current_file = frame.f_code.co_filename
        current_file_name = os.path.basename(frame.f_code.co_filename)
        function_name = frame.f_code.co_name
        line_no = frame.f_lineno

        # 清理旧数据
        clean_old_entries()
        if current_file not in printed_files:
            last_print_time[current_file] = time.time() * 1000  # 转换为毫秒
            printed_files[current_file] = 1
            #print(f"caller: {current_file}")
            #print(f"caller: {current_file},function:{function_name},lineno:{line_no}")
            """
        
            logger = get_logger()
            logger.debug(f"caller: {current_file}")
            """
        else:
            printed_files[current_file] += 1
            current_time_ms = time.time() * 1000  # 当前时间（毫秒）
            # 检查时间间隔
            if (current_time_ms - last_print_time[current_file]) >= output_threshold_ms:
                last_print_time[current_file] = current_time_ms
                #print(f"caller: {current_file}")
                print(f"caller: {current_file},function:{function_name},lineno:{line_no}")
                """
        
                logger = get_logger()
                logger.debug(f"caller: {current_file}")
                """

    return trace_calls_04

# 占位 - dummy
def trace_calls_05(frame, event, arg):
    global last_printed_file
    global printed_files
    global last_print_time

    if event == 'call':
        # 跳过冻结的模块 - 这个方法虽然能提前得知文件名，但是该来的冗余信息还是会来
        if frame.f_code.co_filename.startswith('<frozen'):
            return

        current_file = frame.f_code.co_filename
        current_file_name = os.path.basename(frame.f_code.co_filename)
        function_name = frame.f_code.co_name
        line_no = frame.f_lineno

        print(f"caller:{current_file_name},func:{function_name},line:{line_no}")

    return trace_calls_05

# 综合过滤，什么手段都上
def trace_calls_06(frame, event, arg):
    global last_printed_file
    global printed_files
    global last_print_time

    if event == 'call':
        """
        current_file_name = os.path.basename(frame.f_code.co_filename)
        function_name = frame.f_code.co_name
        line_no = frame.f_lineno
        print(f"[HEAD]:current_file_name:{current_file_name},function:{function_name},lineno:{line_no}")
        """

        # 跳过冻结的模块 - 这个方法虽然能提前得知文件名，但是该来的冗余信息还是会来
        #while frame.f_code.co_filename.startswith('<frozen'):
            #frame = frame.f_back
        # 正确处理
        if frame.f_code.co_filename.startswith('<frozen'):
            return

        current_file = os.path.abspath(frame.f_code.co_filename)
        current_file_name = os.path.basename(frame.f_code.co_filename)
        function_name = frame.f_code.co_name
        line_no = frame.f_lineno
        print(f"06:current_file_name:{current_file_name},function:{function_name},lineno:{line_no}")

        # 清理旧数据
        clean_old_entries()
        if current_file not in printed_files:
            last_print_time[current_file] = time.time() * 1000  # 转换为毫秒
            printed_files[current_file] = 1
            #print(f"caller: {current_file}")
            #print(f"caller: {current_file},function:{function_name},lineno:{line_no}")
            """
        
            logger = get_logger()
            logger.debug(f"caller: {current_file}")
            """
        else:
            printed_files[current_file] += 1
            current_time_ms = time.time() * 1000  # 当前时间（毫秒）
            # 检查时间间隔
            if (current_time_ms - last_print_time[current_file]) >= output_threshold_ms:
                last_print_time[current_file] = current_time_ms
                #print(f"caller: {current_file}")
                print(f"caller: {current_file},function:{function_name},lineno:{line_no}")
                """
        
                logger = get_logger()
                logger.debug(f"caller: {current_file}")
                """
        
    return trace_calls_06

def start_tracing():
    sys.settrace(trace_calls_01)

def stop_tracing():
    sys.settrace(None)

def reset_tracing(level=1):
    if level == 1:
        sys.settrace(trace_calls_01)
    elif level == 2:
        sys.settrace(trace_calls_02)
    elif level == 3:
        sys.settrace(trace_calls_03)    
    elif level == 4:
        sys.settrace(trace_calls_04)
    elif level == 5:
        sys.settrace(trace_calls_05)        
    elif level == 6:
        sys.settrace(trace_calls_06)
    else:
        sys.settrace(None)

# 在这里启动追踪
#start_tracing()
#reset_tracing(1)
