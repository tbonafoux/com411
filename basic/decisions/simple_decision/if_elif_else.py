print("Towards which direction should I paint (up, down, left or right)?")
x = input().lower()

if x == "up":
    print(f"I am painting in the {x}ward direction!")
elif x == "down":
    print(f"I am painting in the {x}ward direction!")
elif x == "left":
    print(f"I am painting to the {x}!")
elif x == "right":
    print(f"I am painting to the {x}!")
else:
    print(f"I am painting to the *#SyN{x}ror*#!")