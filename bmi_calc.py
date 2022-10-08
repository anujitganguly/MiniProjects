# Input Height & Weight
height = float(input("Enter height in CM: "))
weight = float(input("Enter weight in KG: "))

# Calculate & print BMI
height = height/100
bmi = weight/(height*height)
print("Your Body Mass Index(BMI) is: ", bmi)

# Condition of BMI
if bmi > 0:
    if (bmi <= 16):
        print("You are severely underweight")
    elif (bmi <= 18.5):
        print("You are underweight")
    elif (bmi <= 25):
        print("You are healthy")
    elif (bmi <= 30):
        print("You are overweight")
    else:
        print("You are severely overweight")
else:
    print("Enter valid details")