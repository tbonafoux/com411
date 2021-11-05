def pattern():
    sequence = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequence


def display_keys(data):
    for item in data:
        print(item)


def display_values(data):
    print("Values:")
    for item in data:
        print(data[item])


def display_items(data):
    for item in data:
        print(item, data[item])


def run():
    data = pattern()
    display_keys(data)
    display_values(data)
    display_items(data)

if __name__ == "__main__":
    run()