Name = input("enter your name: ")
Name = Name.strip().title()

weight = float(input("enter your weight in kg: "))

height = int(input ("enter your height in cm: "))
height_m = height / 100

bmi = weight / (height_m ** 2)

water = weight * 0.033

print("----------------------")
print(f"Hi {Name}")
print(f"{'BMI':<15}: {bmi:.1f}")
print(f"{'Water / day':<15}: {water:.2f}")
print("----------------------")
