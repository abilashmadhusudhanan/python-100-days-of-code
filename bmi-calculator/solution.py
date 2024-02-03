weight = int(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# ** means power
bmi = (weight / (height ** 2))

print("")
print("Your Body Mass Index(BMI): " + str(bmi))