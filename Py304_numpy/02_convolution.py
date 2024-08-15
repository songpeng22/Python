# -*- coding: utf-8 -*-
# @Time    : 2024/08/12
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py304_numpy\02_convolution.py
# @Desc    : numpy卷积
#          : 卷积核就是图像处理时，给定输入图像，输入图像中一个小区域中像素加权平均后成为输出图像中的每个对应像素。
#          : 其中权值由一个函数定义，这个函数称为卷积核。

import numpy as np

# 定义输入图像和卷积核
image = np.array([[1, 2, 3, 0],
                   [0, 1, 2, 1],
                   [1, 0, 1, 2],
                   [0, 1, 0, 1]])

kernel = np.array([[1, 0],
                   [0, -1]])

# 获取图像和卷积核的形状
image_height, image_width = image.shape
kernel_height, kernel_width = kernel.shape

# 计算输出图像的尺寸
output_height = image_height - kernel_height + 1
output_width = image_width - kernel_width + 1
output = np.zeros((output_height, output_width))

# 卷积操作
for i in range(output_height):
    for j in range(output_width):
        output[i, j] = np.sum(image[i:i + kernel_height, j:j + kernel_width] * kernel)

print(output)