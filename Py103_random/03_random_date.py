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

def get_choice(manual_choice=-1):
    list = []
    list.append(0)
    list.append(1)
    list.append(2)
    list.append(3)

    #weights = [5,3,1,1]
    weights = [5,3,1,1]

    return random.choices(list,weights)[0] if manual_choice == -1 else manual_choice

def get_choice(list = [0,1,2,3], weights = [5,3,1,1], manual_choice=-1):
    return random.choices(list,weights)[0] if manual_choice == -1 else manual_choice

def get_format(index):
    format_list_01 = []
    format_list_02 = []
    
    #
    format_list_01.append('%Y/%m/%d')
    format_list_01.append('%Y.%m.%d')
    format_list_01.append('%Y%m%d')
    format_list_01.append('%Y年%m月%d日')
    #
    format_list_02.append('%Y/%m/')
    format_list_02.append('%Y.%m.')
    format_list_02.append('%Y%m%d')
    format_list_02.append('%Y年%m月')

    #
    if index >= len(format_list_01):
        return ("","")

    return (format_list_01[index],format_list_02[index])

# 生成一个前后五年内的随机日期
def generate_random_date():
    start_date = datetime.now() - timedelta(days=5*365)  # n年前
    end_date = datetime.now() + timedelta(days=3*365)    # n年后
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date #random_date.strftime('%Y/%m/%d')

if __name__ == "__main__":
    #自定义index列表和权重列表
    choice = get_choice([0,1,2,3,4,5],[1,2,3,4,5,10])
    print(f"choice:{choice}")
    # 默认四种选择的随机
    choice = get_choice()
    print(f"choice:{choice}")
    # 0 - '%Y/%m/%d'
    # 1 - '%Y.%m.%d'
    # 2 - '%Y%m%d'
    # 3 - '%Y年%m月%d日'
    # 只做1，2两种选择
    choice = get_choice([1,2],[2,8])
    print(f"choice:{choice}")
    format_01,format02 = get_format(choice)
    print(f"format_01:{format_01}")
    print(f"format02:{format02}")
    date = generate_random_date()
    date01 = date
    date02 = date + relativedelta(years=2)
    text_of_production_date = date01.strftime( format_01 )
    text_of_expiry_date = date02.strftime( format02 )
    print(f"text_of_production_date:{text_of_production_date}")
    print(f"text_of_expiry_date:{text_of_expiry_date}")