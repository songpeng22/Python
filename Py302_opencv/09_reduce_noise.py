# -*- coding: utf-8 -*-
# @Time    : 2024/08/15
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py302_opencv\09_reduce_noise.py
# @Desc    : 滤波降噪

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread('..\images\zhenyu_001.jpg')

# 均值滤波
# 用3*3的核对图片进行卷积操作，核上的参数都是1/9，达到均值的效果
blur = cv2.blur(img, (3, 3))
# 方框滤波（归一化）=均值滤波
box1 = cv2.boxFilter(img, -1, (3, 3), normalize=True)
# 方框滤波（不归一化）
box2 = cv2.boxFilter(img, -1, (3, 3), normalize=False)
# 高斯滤波
# 用5*5的核进行卷积操作，但核上离中心像素近的参数大。
guassian = cv2.GaussianBlur(img, (5, 5), 1)
# 中值滤波
# 将某像素点周围5*5的像素点提取出来，排序，取中值写入此像素点。
mean = cv2.medianBlur(img, 5)

# 展示效果
titles = ['Original figure', 'blur', 'box_norm', 'box_no_norm', 'guassian', 'mean']
images = [img, blur, box1, box2, guassian, mean]
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
