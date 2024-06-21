from PIL import Image
#打开一图片文件
im = Image.open("../images/med_box.jpeg")
#要显示图像需要调用 show()方法
im.show()