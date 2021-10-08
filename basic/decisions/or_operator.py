print("What type of adventure?")
adventure = input().lower()

if adventure == "scary" or adventure == "short":
    print("Entering the dark forest!")
elif adventure == "long" or adventure == "safe":
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")
