import random
print("**\n"
      "\tLet's find your Lucky number\n"
      "\t   \t\t\t\t\t\t\t**\n")
print("Between 0 and 10 ... maybe more? How high shall we go? You tell me")
x = int(input())

y = random.randrange(0, x)
padding = len(str(y))
y_text = str(y)
print("So you lucky number is... \n"
      "      /  \n"
      "    __o____\____ \n"
      "   /._______o__.\ \n"
      "   |'-=-=-=-=-='| \n"
      "   |\  /\  /\  /| \n"
      "   | \/  \/  \/ | \n"
      "   \/-=-=-=-=-=\/ \n"
      "    \"\"\"\"\"\"\"\"\"\"` \n"

      f"   ****{'*'*padding}****\n"
      f"   *   {' '*padding}   *\n"
      f"   *   {y_text.center(padding)}   *\n"
      f"   *   {' '*padding}   *\n"
      f"   ****{'*'*padding}****\n")