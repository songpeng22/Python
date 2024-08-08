import cv2
import matplotlib.pyplot as plt

"""
二值图像：只有黑色和白色两种颜色的图像。 每个像素点可以用 0/1 表示,0 表示黑色,1 表示白色。
灰度图像：只有灰度的图像。 每个像素点用 8bit 数字 [0,255] 表示灰度,如: 0 表示纯黑,255 表示纯白。
彩色图像：彩色图像通常 采用红色(R)、绿色(G)和蓝色(B)三个色彩通道的组合表示。
cv.THRESH_BINARY        表示大于阈值时置 255,否则置 0。
cv.THRESH_BINARY_INV    表示大于阈值时置 0,否则置 255。
cv.THRESH_TRUNC         表示大于阈值时置为阈值 thresh,否则不变(保持原色)。
cv.THRESH_TOZERO        表示大于阈值时不变(保持原色),否则置 0。
cv.THRESH_TOZERO_INV    表示大于阈值时置 0,否则不变(保持原色)。
cv.THRESH_OTSU          表示使用 OTSU 算法选择阈值。
"""
img = cv2.imread('..\images\Collect_057.png',0) #直接读为灰度图像
ret,thresh1 = cv2.threshold(img,60,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles = ['img','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()