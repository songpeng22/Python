# -*- coding: utf-8 -*-
# @Time    : 2024/08/12
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py005_array_list_operation\03_weighted_average.py
# @Desc    : 加权平均

def weighted_average(values, weights):
    """
    计算加权平均数
    :param values: 数值列表
    :param weights: 权重列表
    :return: 加权平均数
    """
    if len(values) != len(weights):
        raise ValueError("values和weights的长度必须相等")
    total_weight = sum(weights)
    # zip将values和weights变成元组的列表，即[(10, 1), (20, 2), (30, 3)]
    # 然后将每个元组的数值与权重相乘，即加权，最终相加在一起
    weighted_sum = sum(value * weight for value, weight in zip(values, weights))
    # 加权平均
    return weighted_sum / total_weight

# 示例
values = [10, 20, 30]
weights = [1, 2, 3]
result = weighted_average(values, weights)
print("加权平均数为：", result)