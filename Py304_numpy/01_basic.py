# -*- coding: utf-8 -*-
# @Time    : 2024/08/12
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py304_numpy\01_basic.py
# @Desc    : numpy入门
#          : Numpy 可以產生一維、二維陣列進行向量（vector）和矩陣（matrix）運算，其在大量運算時有非常優異的效能。

# 引入套件，使用 as 代表別名，可以讓我們少打一點字
import numpy as np

# 陣列元素可以使用 list 或 tuple 傳入
A = np.array([4, 5, 6])
B = np.array((1, 2, 3))

# 印出結果
print(A)
print(B)

# 印出型別
print(type(A))
print(type(B))

# 更改資料
A[0] = 12
B[0] = 7

# 印出更改結果
print(A)
print(B)
