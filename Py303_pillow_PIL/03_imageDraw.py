from PIL import Image, ImageDraw, ImageFont
#使用颜色的十六进制格式
image=Image.new('RGB',(300,200),color="white")

# 创建一个绘图对象
draw = ImageDraw.Draw(image)

# 绘制矩形
draw.rectangle([50, 50, 150, 150], outline='blue', width=3)

# 绘制圆形
draw.ellipse([70, 70, 130, 130], outline='red', width=3)

# 添加文本
draw.text((50, 160), 'Hello, World!', fill='black', font=ImageFont.truetype('arial.ttf', 24))

# 显示图像
image.show()