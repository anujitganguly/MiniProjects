# Import Random Library
import random

# Password size
leng = int(input("Enter size of Password: "))

# Values from where data will be taken for password creation
data = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?abcdefghijklmnopqrstuvwxyz"

# Actual calculation and printing output
passw = "".join(random.sample(data,leng ))
print(passw)