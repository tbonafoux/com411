import csv

records = []
headings = []

def load_data(path):
    global headings
    print("Loading data", end = "")
    with open(path, mode="r") as file:
        csv_read = csv.reader(file, delimiter=',', quotechar='"')
        headings = next(csv_read)
        for row in csv_read:
            records.append(row)
    print("Done!")


def display_menu():
    print("Please select one of the following options:\n"
          "[1] Display the names of all passengers\n"
          "[2] Display the number of passengers that survived\n"
          "[3] Display the number of passengers per gender\n"
          "[4] Display the number of passengers per age group\n")
    user_selection = int(input())
    print(f"You have selected option {user_selection}")
    return user_selection


def display_passenger_names():
    global records
    print("The names of the passengers are...\n")
    for read_row in records:
        print(read_row[3])


def display_number_survived():
    global records
    num_survived = 0
    for survived in records:
        if int(survived[1]) == 1:
            num_survived +=1
    print(f"{num_survived} passengers survived")


def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")
    user_selection = display_menu()
    if user_selection == 1:
        display_passenger_names()
    elif user_selection == 2:
        display_number_survived()
    elif user_selection == 3:
        print("no")
    elif user_selection == 4:
        print("no")
    else:
        print("Error! Option not recognised!")

if __name__ == "__main__":
    run()
