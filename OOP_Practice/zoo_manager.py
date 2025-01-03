class Animal:
    def __init__(self, name, species, sound='Animal sound'):
        self.name = name
        self.species = species
        self.sound = sound

    def get_name(self, name):
        return (f"This animal is named {self.name}")

    def get_species(self, species):
        return (f"This animal is a {self.species}")

    def speak(self):
        return self.sound

class Mammal(Animal):
    def __init__(self, name, species, sound=None):
        super().__init__(name, species, sound)

    def give_birth(self):
        return (f"{self.name} the {self.species} has given birth")

class Bird(Animal):
    def __init__(self, name, species, wingspan=None, sound=None):
        super().__init__(name, species, sound)
        self.wingspan = wingspan
        Aviary.birds.append(self)

    def get_wingspan(self, name, wingspan):
        return (f"The wingspan of the {self.name} is {self.wingspan} meters.")

class Reptile(Animal):
    def __init__(self, name, species, sound=None):
        super().__init__(name, species, sound)
        ReptileEnclosure.reptiles.append(self)

    def bask_in_sun(self):
        return (f"{self.name} the {self.species} is basking in the sun")     

class Primate(Mammal):
    def __init__(self, name, species, sound=None):
        super().__init__(name, species, sound)

    def climb_trees(self):
        return (f"{self.name} the {self.species} is climbing trees")

class Marsupial(Mammal):
    def __init__(self, name, species, sound=None):
        super().__init__(name, species, sound)

    def carry_baby(self):
        return (f"{self.name} the {self.species} is carrying its baby")

class Aviary(Bird):
    birds = []
    def __init__(self):
        pass

class ReptileEnclosure(Reptile):
    reptiles = []
    def __init__(self):
        pass


