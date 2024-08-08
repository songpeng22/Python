# -*- coding: utf-8 -*-
# @Time    : 2024/07/01
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py302_opencv\01_imshow.py
# @Desc    : 以仿射变换的方式，旋转图片

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('..\images\med_box.jpeg')

# 显示原始图像
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.show()

# 图像的尺寸
rows, cols, ch = image.shape

# 选择三个点
#01 openai给的旋转倾斜的例子
#pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
#pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
#02 - 原图不变
#pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
#pts2 = np.float32([[50, 50], [200, 50], [50, 200]])
#03 - diy变化 略微倾斜
#pts1 = np.float32([[0, 0], [200, 0], [0, 200]])
#pts2 = np.float32([[0, 0], [200, 10], [10, 200]])
#04 - diy变化 旋转90度 - 结果成功旋转了，但是也丢失了一部分图像
pts1 = np.float32([[0, 0], [200, 0], [0, 200]])
pts2 = np.float32([[200, 0], [200, 200], [0, 0]])

# 计算仿射变换矩阵
M = cv2.getAffineTransform(pts1, pts2)

# 应用仿射变换
transformed_image = cv2.warpAffine(image, M, (cols, rows))

# 显示变换后的图像
plt.imshow(cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB))
plt.title('Transformed Image')
plt.show()