class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is  {self.name}. I am {self.age} years old")

    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a Dog. My name is  {self.name}. I am {self.age} years old")

    def make_sound(self):
        print("Bow")

cat1 =Cat("Dodo",2.5)
Dog1 =Dog("Tyson",8)

for animal in (cat1,Dog1):
        animal.make_sound()
        animal.info()