phrase = input("What phrase do you see?\n")

print("Reversing...")
reverse = ""

for x in phrase:
    reverse = x + reverse

print(reverse)
