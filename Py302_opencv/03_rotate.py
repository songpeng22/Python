import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('..\images\med_box.jpeg')
image90 = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
# 读取图像的三维（宽/高/颜色）
print(image.shape)
# 显示原始图像
cv2.imshow('image',image)
cv2.imshow('image90',image90)
cv2.waitKey(0)