print("What is your name human?")
name = input()

print("How old are you (in years)?")
age = input()

print("How tall are you (in meters)?")
h = float(input())

print("How much do you weigh (in kilograms)?")
weight = int(input())
bmi = float(weight/h**2)

if bmi > 30:
    print(f'{name} you are {age} years old and you are very round.')
else:
    print(f'{name} you are {age} years old and your bmi is {round(bmi, 2)}.')
