seq = input("Please enter a sequence of 2 symbols")
marker = input("Please enter the marker symbol")
ans = 0
start = 0
for x in seq:
    if x == marker:
        start += 1
    elif start == 1:
        ans += 1
    elif start > 1:
        break

print(f"The distance between the markers is {ans}.")
