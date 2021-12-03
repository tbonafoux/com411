import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frame):
    global ax
    plt.cla()
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.plot(frame, frame, "ro")


def run():
    global fig
    animation_2 = animation.FuncAnimation(fig, animate, frames=10, interval=1000)
    plt.show()


run()
