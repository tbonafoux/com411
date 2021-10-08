print("Please enter the first number.")
x = int(input())
print("Please enter the second number.")
y = int(input())

if x < y:
    print( "The first number is the smallest!")
elif y < x:
    print( "The second number is the smallest!")
else:
    print("Both are equal!")