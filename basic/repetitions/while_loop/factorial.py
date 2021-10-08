num = int(input("Please enter a number:\n"))
x = 0
ans = 1

while x < num:
    x += 1
    ans = ans*x

print(f"The factorial is {ans}")
