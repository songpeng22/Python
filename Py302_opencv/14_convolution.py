# -*- coding: utf-8 -*-
# @Time    : 2024/08/12
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py302_opencv\14_convolution.py
# @Desc    : opencv卷积

import cv2
import numpy as np

# 定义输入图像和卷积核
image = np.array([[1, 2, 3, 0],
                   [0, 1, 2, 1],
                   [1, 0, 1, 2],
                   [0, 1, 0, 1]], dtype=np.float32)

kernel = np.array([[1, 0],
                   [0, -1]], dtype=np.float32)

# 使用 OpenCV 的 filter2D 进行卷积
output = cv2.filter2D(image, -1, kernel)

print(output)