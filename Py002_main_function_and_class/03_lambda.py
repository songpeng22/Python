# -*- coding: utf-8 -*-
# @Time    : 2024/08/16
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py002_main_function_and_class\03_lambda.py
# @Desc    : 将lambda表达式作为函数参数传入

def apply_lambda(func, value):
    return func(value)

# main
if __name__ == '__main__':
    # 使用 lambda
    result = apply_lambda(lambda x: x + 10, 5)
    print(result)  # 输出 15
    