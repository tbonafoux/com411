level = int(input("What level of brightness is required?\n"))
print("\n Adjusting brightness...\n")

for x in range(2, level, 2):
    print(f"Beep's brightness level: {'*'*x}")
    print(f"Boop's brightness level: {'*'*x}\n")

print("Adjustments complete!")