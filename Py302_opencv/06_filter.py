# -*- coding: utf-8 -*-
# @Time    : 2024/07/01
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py302_opencv\01_imshow.py
# @Desc    : 高斯滤波

import cv2
import numpy as np

# 载入图像
img = cv2.imread('..\images\med_box.jpeg')

# 使用高斯滤波进行图像平滑处理
blur = cv2.GaussianBlur(img,(5,5),0)

# 显示处理结果
cv2.imshow('blur',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()