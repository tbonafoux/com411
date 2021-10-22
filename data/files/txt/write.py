def search(path):
    print("Searching...", end = "")
    sections = ""
    books = "Books:\n"
    with open(path) as file:
        for line in file:
            if line.startswith("Section"):
                sections = sections + line
            else:
                books = books + line
    print("Done!")
    return f"{sections}\n\n{books}"


def save(path, text):
    print("Saving...", end = "")
    with open(path, "w") as file:
        file.write(text)
    print("Done!")


def run():
    data = search("books.txt")
    save("section-books.txt", data)

run()