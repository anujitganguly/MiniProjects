# Import needed library
from PIL import Image

# Creating a function to perform actual transformation
def imagePdf(filename, output):
    images = []

    for file in filename:
        im = Image.open(file)
        im = im.convert('RGB')
        images.append(im)

        images[0].save(output, save_all= True, append_images = images[1:])


m = str(input("Enter name of the image with extension: "))
imagePdf([m], "output.pdf")

### This can be re-designed to input multiple images as per user input