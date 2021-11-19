import matplotlib.pyplot as plt

def read_data():
    temps = []
    with open("temps.txt") as file:
        lines = file.readlines()
        for line in lines[1:]:
            temps.append(int(line))
    return temps

def run():
    data = read_data()
    fig, axs = plt.subplots(1, 2, sharey="row")

    days = range(len(data))
    axs[0].plot(days, data)
    axs[1].bar(days, data)
    axs[0].set_ylim(min(data), max(data))
    axs[1].set_ylim(min(data), max(data))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run()
