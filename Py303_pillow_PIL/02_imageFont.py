from PIL import Image, ImageDraw, ImageFont
import cv2

# Create a new image with a white background
width = 800
height = 600
image = Image.new('RGB', (width, height), color = 'white')

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Load a TrueType or OpenType font file, and set the font size
font_root_path = "E:\\PaddleOCR_fonts\\"
font_Codystar_Light = font_root_path + "Codystar-Light-3.ttf"
font_Codystar_Regular = font_root_path + "Codystar-Regular-2.ttf"
font_Snapix = font_root_path + "snapix-1.ttf"
font_Ventouse = font_root_path + "Ventouse-1.ttf"
#font_BPdotsLight = font_root_path + "BPdotsLight.otf"
#font_BPdotsDiamondLight = font_root_path + "BPdotsDiamondLight.otf"
font_BPdotsLight = font_root_path + "BPdotsUnicase.otf"
font_BPdotsDiamondLight = font_root_path + "BPdotsUnicaseLight.otf"
font_Perfograma = font_root_path + "Perfograma.otf"
font_serif_dot_digital = font_root_path + "serif_dot_digital-7.ttf"
font_led_counter = font_root_path + "led_counter-7.ttf"
#font = ImageFont.truetype("arial.ttf", 40)
#font = ImageFont.truetype("Codystar", 40)
offset = 65
position_x = 10
position_y = 10
column_02_y = 450
font_size = 48

# font 01
font = ImageFont.truetype(font_Codystar_Light, font_size)
# Define the text and position
text = "Codystar L"
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 02
font = ImageFont.truetype(font_Codystar_Regular, font_size)
# Define the text and position
text = "1-Codystar R"
position_y += offset
codestar_y = position_y
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 03
font = ImageFont.truetype(font_Snapix, font_size)
# Define the text and position
text = "snapix"
position_y += offset
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 04
font = ImageFont.truetype(font_Ventouse, font_size)
# Define the text and position
text = "Ventouse"
position_y += offset
ventouse_y = position_y
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 05
font = ImageFont.truetype(font_BPdotsLight, font_size)
# Define the text and position
text = "BPdots L"
position_y += offset
BPdotsLight_y = position_y
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 06
font = ImageFont.truetype(font_BPdotsDiamondLight, font_size)
# Define the text and position
text = "BPdotsDiamondL"
position_y += offset
BPdotsDiamondLight_y = position_y
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 07
font = ImageFont.truetype(font_Perfograma, font_size)
# Define the text and position
text = "2-Perfograma"
position_y += offset
Perfograma_y = position_y
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 08
font = ImageFont.truetype(font_serif_dot_digital, font_size)
# Define the text and position
text = "serif_dot_d"
position_y += offset
serif_dot_digital_y = position_y
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 09
font = ImageFont.truetype(font_led_counter, font_size)
# Define the text and position
text = "3-led_counter"
position_y += offset
led_counter_y = position_y
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 12
font = ImageFont.truetype(font_Codystar_Regular, font_size)
# Define the text and position
text = "2024/05/01"
position_x = column_02_y
position_y = codestar_y
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 14
font = ImageFont.truetype(font_Ventouse, font_size)
# Define the text and position
text = "2024/05/01"
position_x = column_02_y
position_y = ventouse_y
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 15
font = ImageFont.truetype(font_BPdotsLight, font_size + 10)
# Define the text and position
text = "2024/05/01"
position_y = BPdotsLight_y
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 16
font = ImageFont.truetype(font_BPdotsDiamondLight, font_size + 10)
# Define the text and position
text = "2024/05/01"
position_y = BPdotsDiamondLight_y
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 17
font = ImageFont.truetype(font_Perfograma, font_size)
# Define the text and position
text = "2024/05/01"
position_y = Perfograma_y
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 18
font = ImageFont.truetype(font_serif_dot_digital, font_size)
# Define the text and position
text = "2024/05/01"
position_y = serif_dot_digital_y
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# font 19
font = ImageFont.truetype(font_led_counter, font_size)
# Define the text and position
text = "2024/05/01"
position_y = led_counter_y
position = (position_x, position_y)
# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# show image
"""
"""
import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()
cv2.waitKey(0)


# Save the image
image.save("./output.png")
