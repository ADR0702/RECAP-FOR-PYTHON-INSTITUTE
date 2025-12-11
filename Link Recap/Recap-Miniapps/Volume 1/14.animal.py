class Animal:
    def __init__(self, name, species):
        self.name=name
        self.species=species
    def speak(self):
        print(f"My name is {self.name} and I am a {self.species}.")
    

animal1=Animal("Ramses", "Cat")
animal2=Animal("Spot", "Dog")

animal1.speak()
animal2.speak()
        