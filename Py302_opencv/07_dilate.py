import cv2
import numpy as np

# 载入图像
img = cv2.imread('..\images\med_box.jpeg')

# 创建一个5x5的结构元素
kernel = np.ones((5,5),np.uint8)

# 进行膨胀操作
dilation = cv2.dilate(img,kernel,iterations = 1)

# 显示处理结果
cv2.imshow('dilation',dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()