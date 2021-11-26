import matplotlib.pyplot as plt
import csv


def read_data():
    with open("titanic.csv") as file:
        raw_data = csv.reader(file)
        data_dict = {"survived": [], "age": [], "fare": [], "sex": []}
        headers = next(raw_data)
        for row in raw_data:
            survived = row[1].strip()
            age = row[4].strip()
            fare = row[8].strip()
            sex = row[14].strip()
            if survived != "" and age != "" and fare != "" and sex != "":
                data_dict["survived"].append(bool(int(survived)))
                data_dict["age"].append(float(age))
                data_dict["fare"].append(round(float(fare), 2))
                if sex.lower() == "0":
                    data_dict["sex"].append("male")
                elif sex.lower() == "1":
                    data_dict["sex"].append("female")
    return data_dict


def run():
    data = read_data()
    fig, axs = plt.subplots(2, 2,)
    axs[0, 0].bar(data["sex"], (data["age"]))
    axs[0, 1].bar(data["sex"], data["survived"])
    axs[1, 0].bar(data["sex"], data["fare"])
    axs[1, 1].plot(data["age"], data["survived"])
    plt.show()


if __name__ == "__main__":
    run()
