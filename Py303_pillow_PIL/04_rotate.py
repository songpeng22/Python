from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# 打开一图片文件
image = Image.open("./images/med_box.jpeg")

"""
# 旋转
rotated_image = image.rotate(45)
plt.imshow(rotated_image)
plt.title('Original Image')
plt.show()
"""

# 加亮
enhancer = ImageEnhance.Brightness(image)
bright_image = enhancer.enhance(1.5)
bright_image.show()

#rotated_image.show()
