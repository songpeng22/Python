# -*- coding: utf-8 -*-
# @Time    : 2024/07/01
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py302_opencv\01_imshow.py
# @Desc    : 读取图片，并用pyplot显示出来

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('..\images\med_box.jpeg')
# 读取灰度图像
#image = cv2.imread('.\images\med_box.jpeg',cv2.IMREAD_GRAYSCALE)
# 读取图像的三维（宽/高/颜色）
print(image.shape)
# 显示原始图像
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.show()