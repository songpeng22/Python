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