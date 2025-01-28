# Day 1.2 exercise
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = float(weight) / (float(height) ** 2)
print("Your BMI is ", bmi)
print("Your BMI is ", round(bmi))