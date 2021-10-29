def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run():
    print("Moving...")
    path = movements()
    x = 0
    for step in range(0, len(path), 2):
        print(f"{path[step]} for {path[step+1]} steps")

if __name__ == "__main__":
    run()