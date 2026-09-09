from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self,name,habitat):
        self.name = name
        self.habitat = habitat

    def display(self):
        print(f"Name:{self.name} | Habitat: {self.habitat}")

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self,name,habitat,breed):
        super().__init__(name, habitat)
        self.breed = breed  

    def speak(self):
        print(f"{self.name} ({self.breed}) says: Woof! Woof!")

class Parrot(Animal):

    def __init__(self,name,habitat,phrase):
        super().__init__(name,habitat)
        self.phrase = phrase

    def speak(self):
        print(f"{self.name} says: {self.phrase}! {self.phrase}!")

dog = Dog("Bruno","Home","Labrdor")
parrot = Parrot("Polly",  "Jungle",    "Squawk")

print("=== Animal Sound Show ===\n")
for animal in [dog,parrot]:
    animal.display()
    animal.speak()
    print()