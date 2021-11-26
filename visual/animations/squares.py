import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
squares = []

def init():
    global squares
    squares.append({"x": [3, 3, 4, 4, 3], "y": [3, 4, 4, 3, 3]})
    squares.append({"x": [2, 2, 5, 5, 2], "y": [2, 5, 5, 2, 2]})
    squares.append({"x": [1, 1, 6, 6, 1], "y": [1, 6, 6, 1, 1]})


def animate(frame):
    global ax
    global squares
    plt.cla()
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.plot(squares[frame]["x"],squares[frame]["y"])


def run():
    global fig
    init()
    animation_2 = animation.FuncAnimation(fig, animate, frames=3, interval=500)
    plt.show()


if __name__ == "__main__":
    run()
