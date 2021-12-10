class Human:

    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'human(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self):
        return f'{self.name} is {self.age} years old and has {self.energy} energy.'

    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy = self.energy + amount
        if self.energy > self.MAX_ENERGY:
            self.energy = self.MAX_ENERGY

    def move(self, distance):
        if self.energy < distance:
            print(f"{self.name} can't go that far.\n"
                  f"{self.name} has moved {self.energy} out of {distance}")
            self.energy = 0
        else:
            self.energy = self.energy-distance


if __name__ == "__main__":
    human = Human()
    human.display()
    print(human)
    print(repr(human))
