import logging
from datetime import datetime
from logger import get_logger

"""
# 创建一个logger对象
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# 获取当前时间并格式化为字符串
current_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
# 生成输出文件路径
output_dir = 'C:\\Users\\songp\\Desktop\\test\\'
output_file_path = output_dir + current_time + ".txt"
# 创建file handler
file_handler = logging.FileHandler(output_file_path)
file_handler.setLevel(logging.DEBUG)

# 创建stream handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(file_handler)
logger.addHandler(console_handler)
"""
if __name__ == "__main__":
    logger = get_logger()
    # 记录日志
    logger.debug('这是一条debug级别的日志')
    logger.info('这是一条info级别的日志')
    logger.warning('这是一条warning级别的日志')
    logger.error('这是一条error级别的日志')
    logger.critical('这是一条critical级别的日志')
    #get logger again
    logger = get_logger()
    logger.critical('get logger again')