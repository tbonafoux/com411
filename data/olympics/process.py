import tui

def list_years(data):
    years = set()
    for row in data:
        years.add(row[10])
    tui.completed()
    return years


def tally_medals(data):
    {"Gold": 0, "Silver": 0, "Bronze": 0}
    for row in data:
        if row[15]


def tally_team_medals(data):
    pass


list_years({"apple", "banana", "cherry", "banana"})
