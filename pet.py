class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        # Reduce hunger, but not below 0
        self.hunger -= 3
        if self.hunger < 0:
            self.hunger = 0
        # Increase happiness
        self.happiness += 1
        if self.happiness > 10:
            self.happiness = 10
        print(self.name + " ate some food.")

    def sleep(self):
        # Increase energy, but not above 10
        self.energy += 5
        if self.energy > 10:
            self.energy = 10
        print(self.name + " had a nice nap.")

    def play(self):
        # Only play if the pet has enough energy
        if self.energy >= 2:
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1

            # Keep values in range
            if self.happiness > 10:
                self.happiness = 10
            if self.hunger > 10:
                self.hunger = 10

            print(self.name + " played and had fun!")
        else:
            print(self.name + " is too tired to play.")

    def get_status(self):
        print("Pet Name:", self.name)
        print("Hunger:", self.hunger)
        print("Energy:", self.energy)
        print("Happiness:", self.happiness)

    def train(self, trick):
        self.tricks.append(trick)
        print(self.name + " learned to " + trick + "!")

    def show_tricks(self):
        if self.tricks:
            print(self.name + " knows these tricks:", ", ".join(self.tricks))
        else:
            print(self.name + " hasn't learned any tricks yet.")
