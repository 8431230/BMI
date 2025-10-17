weight = float(input("Enter weight (in kg): "))
height = float(input("Enter height (in meters): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("Weight:", weight, "kg")
print("Height:", height, "m")
print("BMI:", round(bmi, 2))
print("Category:", category)


