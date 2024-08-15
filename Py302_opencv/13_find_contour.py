# -*- coding: utf-8 -*-
# @Time    : 2024/08/12
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py302_opencv\013_find_contour.py
# @Desc    : 寻找轮廓

import cv2
import numpy as np
import os

# 读取图像
image_name = "Collect_057.png"
#image_name = "face.jpg"
relative_path = "..\\images\\" + image_name
image_path = os.path.dirname(__file__) + "/" + relative_path
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转换为灰度图
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # 二值化处理

# 查找轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 在原图上绘制轮廓
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)  # 绿色轮廓，线宽为2

# 显示结果
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()