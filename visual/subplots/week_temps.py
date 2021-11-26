import matplotlib.pyplot as plt
import csv


def read_data():
    with open("temps.csv") as file:
        csv_reader = csv.reader(file, delimiter=',', quotechar='"')
        header = next(csv_reader)
        data = {}
        col_1_data = []
        col_2_data = []
        for row in csv_reader:
            col_1_data.append(int(row[0]))
            col_2_data.append(int(row[1]))
        data[header[0]] = col_1_data
        data[header[1]] = col_2_data
        return data


def run():
    data = read_data()
    fig, axs = plt.subplots(2, 1, sharex="col")
    keys = list(data.keys())
    print(data.keys())
    days = range(len(data[keys[0]]))
    axs[0].plot(days, data["week1"])
    axs[1].bar(days, data["week2"])
    plt.show()


if __name__ == "__main__":
    run()
