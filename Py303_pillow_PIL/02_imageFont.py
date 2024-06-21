from PIL import Image, ImageDraw, ImageFont
import cv2

# Create a new image with a white background
image = Image.new('RGB', (200, 100), color = 'white')

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Load a TrueType or OpenType font file, and set the font size
font = ImageFont.truetype("arial.ttf", 40)

# Define the text and position
text = "Hello, PIL!"
position = (10, 10)

# Draw the text on the image
draw.text(position, text, font=font, fill="black")

# show image
"""
import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()
cv2.waitKey(0)
"""

# Save the image
image.save("output.png")
