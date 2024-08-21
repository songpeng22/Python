import cv2
import numpy as np
import os

def connect_dots(image_path):
    # 加载图像并转换为灰度图
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 二值化图像，提取接近黑色的点
    _, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)

    # 找到所有的点
    points = np.argwhere(binary)

    # 创建一个空白图像用于绘制连接线
    connected_image = np.zeros_like(image)

    # 连接相邻的点
    for i in range(len(points) - 1):
        y1, x1 = points[i]
        y2, x2 = points[i + 1]

        # 计算距离
        distance = np.linalg.norm((x1 - x2, y1 - y2))

        # 连接条件：可以调整连接的最大距离
        if distance <= 15:
            cv2.line(connected_image, (x1, y1), (x2, y2), (255, 255, 255), 1)

    # 将原图与连接后的图像合并
    result = cv2.addWeighted(image, 0.5, connected_image, 1.0, 0)

    return result

def find_and_connect_points(binary):
    # 使用形态学操作连接点
    kernel = np.ones((3, 3), np.uint8)
    connected = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    return connected

image_name = "food503.jpg"
relative_path = "..\\images\\" + image_name
image_path = os.path.dirname(__file__) + "/" + relative_path

# 示例用法
if __name__ == "__main__":
    output_image = connect_dots(image_path)
    cv2.imshow('Connected Dots', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
