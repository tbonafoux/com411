def display_chars(path, chars):
    with open(path) as file:
        data = file.read(chars)
        print(f"The first {chars} characters are:\n{data}\n")


def display_line(path):
    with open(path) as file:
        data = file.readline().strip()
        print(f"The 1st line is:\n{data}\n")



def display_text(path):
    with open(path) as file:
        data = file.read()
        print(f"The full text ius:\n {data}\n")



def run():
    x = int(input("How many chars to display?"))
    display_chars("library.txt", x)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run()