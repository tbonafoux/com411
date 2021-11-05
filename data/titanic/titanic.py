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
          "[4] Display the number of passengers per age group\n"
          "[5] Check if the main 2 Titanic movie characters where based on real people\n")
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


def display_passengers_per_gender():
    global records
    females = 0
    males = 0
    for passengers in records:
        if passengers[4] == "male":
            males += 1
        elif passengers[4] == "female":
            females += 1
    print(f"Females: {females}, Males: {males}")


def display_passengers_per_age_group():
    global records
    children = 0
    adults = 0
    elderly = 0
    for passengers in records:
        if (passengers[5]) == "":
            pass
        elif float(passengers[5]) < 18:
            children += 1
        elif float(passengers[5]) < 65:
            adults += 1
        else:
            elderly += 1
    print(f"children: {children}, adults: {adults}, elderly: {elderly}")


def movie_test():
    global records
    rose = False
    jack = False
    for passenger in records:
        if "Rose" in passenger[3] and int(passenger[1] == 1):
            rose = True
    for passenger in records:
        if "Jack" in passenger[3] and int(passenger[1] == 0):
            jack = True
    if rose == True and jack == True:
        print(f"Possibly based on real people")
    else:
        print(f"Not based on real people")

def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records.")
    user_selection = display_menu()
    if user_selection == 1:
        display_passenger_names()
    elif user_selection == 2:
        display_number_survived()
    elif user_selection == 3:
        display_passengers_per_gender()
    elif user_selection == 4:
        display_passengers_per_age_group()
    elif user_selection == 5:
        movie_test()
    else:
        print("Error! Option not recognised!")

if __name__ == "__main__":
    run()
