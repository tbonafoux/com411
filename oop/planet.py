from oop.human import Human
from oop.robot import Robot


class planet:

    humans = []
    robots = []

    def add_human(self, a, b, c):
        a = Human(a, b, c)
        self.humans.append(a)

    def remove_human(self):
        self.humans.remove(Human())

    def add_robot(self):
        self.robots.append(Robot())

    def remove_robot(self):
        self.robots.remove(Robot())

    def __repr__(self):
        return f"Humans; {humans}\n" \
               f"Robots; {Robots}"


planet.add_human("bob", 20, 50)
planet.add_human("rob", 30, 66)
print(repr(planet))
