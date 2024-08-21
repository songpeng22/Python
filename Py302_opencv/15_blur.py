# -*- coding: utf-8 -*-
# @Time    : 2024/08/15
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py302_opencv\15_blur.py
# @Desc    : 模糊处理

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import os

# 读取图像
image_name = "food503.jpg"
relative_path = "..\\images\\" + image_name
image_path = os.path.dirname(__file__) + "/" + relative_path
image_cv2 = cv2.imread(image_path)
image = Image.open(image_path)

# 应用模糊滤镜
filter_blurred_image = image.filter(ImageFilter.BLUR)
blur = cv2.blur(image_cv2, (3, 3))
gauss_blurred_image = cv2.GaussianBlur(image_cv2, (5, 5), 0)
medianBlurre_image = cv2.medianBlur(image_cv2, 5)

# 展示效果
titles = ['Original figure', 'filter_blur', 'blur', 'gauss_blur', 'median_blur']
images = [image, filter_blurred_image, blur, gauss_blurred_image, medianBlurre_image]
for i in range(5):
    # save image
    image_dir = 'E:\\PaddleOCR_Data\\train_data_01_easy_test\\'
    image_path = image_dir + str(i) + ".jpg"
    if isinstance(images[i],Image.Image):
        images[i].save(image_path)
    elif isinstance(images[i],np.ndarray):
        cv2.imwrite(image_path, images[i])
    # draw on pallet
    plt.subplot(2, 3, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
