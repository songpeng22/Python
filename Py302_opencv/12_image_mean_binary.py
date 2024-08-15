# -*- coding: utf-8 -*-
# @Time    : 2024/08/12
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py302_opencv\12_image_mean_binary.py
# @Desc    : 自适应二值化

import cv2
import matplotlib.pyplot as plt
import os

image_path = os.path.dirname(__file__) + "/" + '..\images\Collect_057.png'
image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE) 

#res1 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,5)
#res2 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,5)

# 自适应二值化
adaptive_thresh_01 = cv2.adaptiveThreshold(
    image,                          # 输入图像
    255,                            # 最高阈值
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, # 自适应方法
    cv2.THRESH_BINARY,              # 阈值类型
    11,                             # 块大小（必须是奇数）
    2                               # 常数C
)

adaptive_thresh_02 = cv2.adaptiveThreshold(
    image,                          # 输入图像
    255,                            # 最高阈值
    cv2.ADAPTIVE_THRESH_MEAN_C,     # 自适应方法
    cv2.THRESH_BINARY,              # 阈值类型
    11,                             # 块大小（必须是奇数）
    2                               # 常数C
)
 
#cv2.imshow('res1',adaptive_thresh)
#cv2.imshow('res2',res2)
titles = ['img','ADAPTIVE_THRESH_GAUSSIAN_C','ADAPTIVE_THRESH_MEAN_C']
images = [image, adaptive_thresh_01, adaptive_thresh_02]
for i in range(3):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
