### This is needed to train Machine Learning Models ###
# The image and the code should be in same folder to run successfully

# Import necessary libraries
from PIL import Image
from numpy import asarray

# User input of Image file
n = input("Enter the image name with extension to find array: ")

# Actual image transformation
image = Image.open(n)
data = asarray(image)
print(data)


## Future Scope: GUI can be added and new feature to browse the specific photo is also possible