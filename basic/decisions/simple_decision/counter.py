print("Please enter the first whole number.")
x = int(input())
print("Please enter the second whole number.")
y = int(input())
print("Please enter the third whole number.")
z = int(input())

list = [x,y,z]
even = 0
odd = 0
for num in list:
    if num % 2 == 0:
        even += 1
    else:
        odd +=1

print(f"There were {even} even and {odd} odd numbers.")