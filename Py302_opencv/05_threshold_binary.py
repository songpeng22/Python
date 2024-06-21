import cv2
import numpy as np

# 载入图像并转为灰度图
img = cv2.imread('..\images\med_box.jpeg')

# 阈值化处理
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# 显示处理结果
cv2.imshow('threshold',thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()