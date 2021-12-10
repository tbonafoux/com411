from human import Human
from robot import Robot


class planet:

    def __init__(self, name = ""):
        self.name = name
        self.occupants = {
            "humans": [],
            "robots": []
        }

    def __repr__(self):
        return f"[{self.name}:\n" \
               f"Humans; {self.occupants['humans']}\n" \
               f"Robots; {self.occupants['robots']}"

    def __str__(self):
        return f"{self.name} has the {len(self.occupants['humans'])} humans and {len(self.occupants['robots'])} robots"

    def add_human(self, human):
        self.occupants["humans"].append(human)

    def remove_human(self, human):
        self.occupants["humans"].remove(human)

    def add_robot(self, robot):
        self.occupants["robots"].append(robot)

    def remove_robot(self, robot):
        self.occupants["robots"].remove(robot)


if __name__ == "__main__":
    dune = planet("Dune")
    print(repr(dune))
    robby = Human("Rob")
    dune.add_human(robby)
    bob = Robot("Bob", 20, 50)
    dune.add_robot(bob)
    beep = Robot("Beep", 100, 20)
    dune.add_robot(beep)
    print(dune)
    dune.remove_robot(beep)
    print(repr(dune))
    print(dune)