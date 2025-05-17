weight = 85
height = 1.85

bmi = weight / (height ** 2)

# Don't change values above
# Write code below

print(bmi)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweght")
