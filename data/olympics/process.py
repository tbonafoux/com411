import tui

def list_years(data):
    tui.started("Listing years.")
    years = set()
    for row in data:
        years.add(row[9])
    tui.display_years(years)
    tui.completed()


def tally_medals(data):
    medal_tally = {"Gold": 0, "Silver": 0, "Bronze": 0}
    tui.started("Tally medals")
    for row in data:
        if row[14] == "Gold":
            medal_tally["Gold"] += 1
        elif row[14] == "Silver":
            medal_tally["Silver"] += 1
        elif row[14] == "Bronze":
            medal_tally["Bronze"] += 1
        else:
            pass
    tui.display_medal_tally(medal_tally)
    tui.completed()


def tally_team_medals(data):
    team_medal_tally = {}
    tui.started("Team medal tally.")
    for row in data:
        if row[14] == "NA":
            pass
        else:
            if row[6] in team_medal_tally:
                if row[14] == "Gold":
                    team_medal_tally[row[6]]["Gold"] += 1
                elif row[14] == "Silver":
                    team_medal_tally[row[6]]["Silver"] += 1
                elif row[14] == "Bronze":
                    team_medal_tally[row[6]]["Bronze"] += 1
            else:
                team_medal_tally[row[6]] = {"Gold": 0, "Silver": 0, "Bronze": 0}
                if row[14] == "Gold":
                    team_medal_tally[row[6]]["Gold"] += 1
                elif row[14] == "Silver":
                    team_medal_tally[row[6]]["Silver"] += 1
                elif row[14] == "Bronze":
                    team_medal_tally[row[6]]["Bronze"] += 1
    tui.display_team_tally(team_medal_tally)
    tui.completed()


