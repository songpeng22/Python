# -*- coding: utf-8 -*-
# @Time    : 2024/08/16
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py103_random\02_random_string.py
# @Desc    : 按照规则，随机生成字符串

import random
import string
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import os


# 定义每个大写字母的出现概率
probabilities = {
    'A': 8,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 12,
    'F': 2,
    'G': 2,
    'H': 6,
    'I': 0, # hard identify, not exist
    'J': 1,    
    'K': 1,
    'L': 4,
    'M': 2,
    'N': 6,
    'O': 0, # hard identify, not exist
    'P': 2,
    'Q': 1,
    'R': 5,
    'S': 6,
    'T': 9,
    'U': 3,
    'V': 1,
    'W': 2,
    'X': 1,
    'Y': 2,
    'Z': 1,           
}

def generate_random_string():
    # 生成前四位大写字母
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    # 生成后四位数字
    numbers = ''.join(random.choices(string.digits, k=4))
    # 拼接并返回最终字符串
    return letters + numbers

def generate_random_charactor_string(letter_probabilities):
    # 生成四位大写字母
    letters = random.choices(
        population=list(letter_probabilities.keys()), 
        weights=list(letter_probabilities.values()), 
        k=2
    )
    
    return ''.join(letters)

def generate_random_number_string():
    numbers = random.choices(string.digits, k=4)
    return ''.join(numbers)

def generate_random_time_string():
    hours = random.randint(0, 23)   # 随机生成小时
    minutes = random.randint(0, 59)  # 随机生成分钟
    #seconds = random.randint(0, 59)  # 随机生成秒钟
    #return f"{hours:02}:{minutes:02}:{seconds:02}"  # 格式化为 HH:MM:SS
    return f"{hours:02}:{minutes:02}"

def generate_random_string():
    string_01 = generate_random_charactor_string(probabilities)
    string_02 = generate_random_number_string()
    string_03 = generate_random_time_string()

    return ''.join(string_01) + ''.join(string_03)

if __name__ == "__main__":
    # generate and combine test string
    serial_string = generate_random_string()
    print(f"serial_string:{serial_string}")
    
