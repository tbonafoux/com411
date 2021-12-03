class Human:

    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy

    def display(self):
        print(f"I am {self.name}")


if __name__ == "__main__":
    human = Human()
    human.display()
