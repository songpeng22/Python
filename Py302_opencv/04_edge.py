# -*- coding: utf-8 -*-
# @Time    : 2024/07/01
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py302_opencv\01_imshow.py
# @Desc    : 边缘检测，类似二值图，将图片中的物体的轮廓画出来

import cv2
import numpy as np

# 载入图像
#药盒 - 文字轮廓
#img = cv2.imread('..\images\med_box.jpeg')
#两辆车 - 车的轮廓
img = cv2.imread('..\images\cars.jpg')

# 进行Canny边缘检测
edges = cv2.Canny(img,100,200)

# 显示处理结果
cv2.imshow('edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()