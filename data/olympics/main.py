import csv
import process
import tui


def read_data(file_path):
    tui.started(f"Reading data from {file_path}")
    with open(file_path) as file:
        data = []
        athlete_data = csv.reader(file)
        head = next(athlete_data)
        for row in (athlete_data):
            data.append(row)
    tui.completed()
    return data

def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu()
        if selection == "years":
            data = read_data("athlete_events.csv")
            process.list_years(data)
        elif selection == "tally":
            data = read_data("athlete_events.csv")
            process.tally_medals(data)
        elif selection == "team":
            data = read_data("athlete_events.csv")
            process.tally_team_medals(data)
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()