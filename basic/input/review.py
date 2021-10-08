# module import for random number generation
import random
# starting program text prompt for input
print("**\n"
      "\tLet's find your Lucky number\n"
      "\t   \t\t\t\t\t\t\t**\n")
print("Between 0 and 10 ... maybe more? How high shall we go? You tell me")
# user upper range input
x = int(input())
# random "lucky number" generation in users range
y = random.randrange(0, x)
# creation of padding to allow proper display of differnt length numbers
padding = len(str(y))
# conversion on int to str to allow centered display
y_text = str(y)
# output statement
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