print("What type of cover does the book have?")
cover = input().lower()

if cover == "soft":
    print("Is the book prefectly bound?")
    binding = input().lower()
    if binding == "yes":
       print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches "
              "are great for short books should be displayed.")
elif cover == "hard":
    print("Books with hard covers can be more expensive!")
else:
    print("I don't know what to do")