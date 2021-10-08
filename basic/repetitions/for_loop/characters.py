marks = input("What strange markings do you see?\n")
print("Identifying...\n")
y=0

for x in marks:
        print(f"index {y}: {x}")
        y += 1

print("Done!")