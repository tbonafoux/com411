# print("How many bars should be charged?")
bars = int(input("How many bars should be charged?\n"))
x = 0

while x < bars:
    x += 1
    print(f"Charging: {'█ '*x}")

print("\nThe battery is fully charged")