print("What is the temperature?")
temp = float(input())
print("Is there rain?")
rain = input().lower()
print("Is it windy?")
wind = input().lower()

# weather condition decider
if rain == "yes":
    if temp > 15 and wind == "no":
        print("Take a brolly")
    elif temp < 15 or wind == "yes":
        if temp < 20:
            print("Take a jacket")
        else:
            print("Take a non-insulated waterproof")
    else:
        print("You might need a jacket or a brolly")
else:
    if temp > 20 and wind == "no":
        print("Shorts and t-shirts time")
    elif temp < -10 or temp > 40:
        print("Stay inside")
    else:
        print("Keep warm")
