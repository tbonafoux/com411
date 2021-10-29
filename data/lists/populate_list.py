def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    options = directions()
    for option in options:
        print(f"{options.index(option)}: {option}")
    user_input = int(input())
    return options[user_input]


def run():
    route = []
    print("Working out escape route...")
    for x in range(0, 5):
        y = menu()
        route.append(y)
    print(f"Route: {route}")


if __name__ == "__main__":
    run()
