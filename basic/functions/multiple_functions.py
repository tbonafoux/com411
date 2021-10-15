def display_ladder(steps):
        print('|_|\n'*steps)

def create_ladder():
        steps = int(input("How many steps remain?\n"))
        display_ladder(steps)

create_ladder()
