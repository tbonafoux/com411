import csv

import process
import tui


def read_data(file_path):
    tui.started(f"Reading data from {file_path}")
    with open(file_path) as file:
        data = []
        cvs = cvs.reader(file)
        for row in cvs:
            data.append(row)
    tui.completed(f"Reading data from {file_path}")
    return data

def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu()
        if selection == "years":
            pass
        elif selection == "tally":
            pass
        elif selection == "team":
            pass
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()