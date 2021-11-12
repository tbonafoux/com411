def started(msg=""):
    print("-"*85)
    print(f"Operatio started: {msg}...\n")


def completed():
    print(f"\n"
          f"Operation completed.\n"
          f"{'-'*85}")


def error(msg):
    print(f"Error! {msg}")


def menu():
    print("Please select one of the following options\n"
          "[years]    List unique years\n"
          "[tally]    Tally up medals\n"
          "[ctally]   Tally up medals for each team\n"
          "[exit]     Exit the program\n")
    user_selection = input()
    return user_selection


def display_medal_tally(tally):
    for item in tally:
        print(f"|{item:<10}| {tally[item]:<10}|")


def display_team_tally(team_tally):
    for item in team_tally:
        print(item)
        print(", ".join("{}:{}".format(k, v) for k, v in team_tally[item].items()))


def display_years(years):
    years_sorted = sorted(years)
    for year in reversed(years_sorted):
        print(year)

