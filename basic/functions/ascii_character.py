char = int(input("Program Started!\n"
             "Please enter an ASCII code:\n"))

if char in range(32,126):
    print(f"The character represented by the ASCII code:{char} is: {chr(char)}\n"
      f"Program Ended!")
else:
    print("Not an ASCII character\n"
          "Program Ended!")