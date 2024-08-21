# -*- coding: utf-8 -*-
# @Time    : 2024/08/16
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py002_main_function_and_class\02_input_function.py
# @Desc    : 将函数作为函数参数传入

def apply_function(func, value):
    return func(value)

# 示例函数
def square(x):
    return x * x

# main
if __name__ == '__main__':
    # 使用
    result = apply_function(square, 5)
    print(result)  # 输出 25
    