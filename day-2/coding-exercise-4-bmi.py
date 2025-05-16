# Enhanced the BMI calculator but asked the user for their height and weight
# then perform the same calcualtion and out put the result

# input values needed to be cast as floats so that the calucation could be done
height = float(input("What is your hieght in meters? "))
weight = float(input("What is your weight in kilograms? "))

# Write you code here.
# Calculate the bmi using weight and height

bmi = weight / (height ** 2)

# When pringint a number just use a comma, no plus symbol
print("Your BMI is: ",bmi)