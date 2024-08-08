# -*- coding: utf-8 -*-
# @Time    : 2024/07/01
# @Author  : peng song
# @Email   : songpeng24@msn.com
# @File    : Py302_opencv\01_imshow.py
# @Desc    : opencv绘图/PIL_IMage绘图

import numpy as np
from PIL import Image, ImageDraw
import cv2

image = None
#生成图片 - np
def numpyLib_create_image_draw_save():
    image = np.zeros((512,512,3), np.uint8)
    # Draw a diagonal blue line with thickness of 5 px
    cv2.line(image,(0,0),(300,300),(255,0,0),5)
    #保存
    image_path = 'C:\\Users\\songp\\Desktop\\test\\test01.jpg'
    write_image_to(image,image_path)
    return image
#生成图片 - Image
def PILImageLib_create_image_draw_save(width = 800,height = 600):
    # Create a new image with a white background
    image = Image.new('RGB', (width, height), color = 'white')
    draw = ImageDraw.Draw(image)
    # 定义线条的起点和终点坐标
    start_point = (0, 0)
    end_point = (250, 250)
    # 定义线条的颜色和宽度
    line_color = (0, 0, 255)  # 红色
    line_width = 5
    draw.line([start_point, end_point], fill=line_color, width=line_width)
    # Save the image
    image_path = 'C:\\Users\\songp\\Desktop\\test\\test02.jpg'
    image.save(image_path)
    return image

def write_image_to(image_handle,image_path):
    cv2.imwrite(image_path, image_handle)

# 显示图像 - opencv
def show_image_by_opencv(image):
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 显示图像 - matplotlib pyplot
def show_image_by_matplotlib_pyplot(image):
    import matplotlib.pyplot as plt
    plt.imshow(image)
    plt.show()
    cv2.waitKey(0)

if __name__ == '__main__':
    # opencv这一套自成系统，不接受PIL的图像，但是可以用matplotlib_pyplot显示
    image_01 = numpyLib_create_image_draw_save()
    #show_image_by_opencv(image_01)
    #show_image_by_matplotlib_pyplot(image_01)

    # PIL image和opencv是两个独立的系统
    image_02 = PILImageLib_create_image_draw_save()
    show_image_by_matplotlib_pyplot(image_01)