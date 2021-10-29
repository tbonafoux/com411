def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction.")
    direction = directions()
    for option in direction:
        print(f"{direction.index(option)}: {option}")


def run():
    menu()


if __name__ == "__main__":
    run()