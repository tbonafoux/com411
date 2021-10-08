dist = int(input("How far are we from the cave?\n"))

for x in range(dist, 0, -1):
    print(f"{x} steps remaining")

print("\nWe have reached the cave!")