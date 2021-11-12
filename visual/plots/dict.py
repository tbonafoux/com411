import matplotlib.pyplot as plt
import random

def data():
    paths = {}
    line_type = input("What type of line would you like to use?(:, -- or -)")
    colour_type = input("What colour line would you like to use?(r, b or g)")
    marker_type = input("What type of marker would you like to use?(o, s or ^)")
    paths["linestyle"] = line_type
    paths["color"] = colour_type
    paths["marker"] = marker_type
    return paths


def generate():
    num_lines = input("How many lines would you like to display?")
    for line in range(int(num_lines)):
        values = data()
        x = random.sample(range(20), k=5)
        y = random.sample(range(20), k=5)
        styles = f"{values['color']}{values['marker']}{values['linestyle']}"
        plt.plot(x,y,styles)


def run():
    print("Running...")
    generate()
    plt.show()
    print("Done")


if __name__ == "__main__":
    run()
