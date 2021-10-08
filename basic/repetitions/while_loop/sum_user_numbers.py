num_of_nums = int(input("How many numbers should I sum up?\n"))
x = 0
ans = 0

while x < num_of_nums:
    x += 1
    ans += int(input(f"Please enter number {x} of {num_of_nums}\n"))

print(f"\nThe answer is {ans}")