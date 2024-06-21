import cv2
import numpy as np

# 载入图像
img = cv2.imread('..\images\med_box.jpeg')

# 进行Canny边缘检测
edges = cv2.Canny(img,100,200)

# 显示处理结果
cv2.imshow('edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()