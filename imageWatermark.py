## Necessary Image should be in the same folder as code
# Importing necessary modules
from PIL import Image, ImageDraw, ImageFont

# Taking user input for image and Watermark text
k = input("Enter image name with extention: ")
text = input("Enter watermark: ")

# Performing image operations
img = Image.open(k)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf', 500)
textwidth, textheight = draw.textsize(text, font)
width, height = img.size

# Position of text
x = width/2 - textwidth/2
y = height - textheight - 1000
draw.text((x, y), text, font = font)

# Output
img.save(r'watermark.png')
Image.open('watermark.png')

# Future Scope: Adding multiple images and transforming all at once