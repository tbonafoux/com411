import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frame):
    global ax

    plt.xlim(0, 720)
    plt.ylim(-1, 1)
    x = list(range(frame))
    y = [math.sin(math.radians(num)) for num in x]
    plt.plot(x, y)


def run():
    global fig
    animation_2 = animation.FuncAnimation(fig, animate, frames=720, interval=50)
    plt.show()


run()
