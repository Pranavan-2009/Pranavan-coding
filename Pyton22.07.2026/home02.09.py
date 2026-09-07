class student:
    grade=10
    print("Hi I am student of grade",grade)

ob=student()

class student:
    grade=10
    name = "penguin"

    def introduction(self):
        print("Hi I am a Student")

    def deatails(self):
        print("My mame is",self.name)
        print("I study in Grade",self.grade)

ob = student()
ob.introduction()
ob.deatails()

class Parrot:
    species = "bird"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

blu = Parrot("Blu",10)
woo = Parrot("woo",15)

print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

print("{}is{}years old".format(blu.name,blu.age))
print("{}is{}years old".format(woo.name,woo.age))

class Parrot:
    
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self,song):
        return"{}sings{}".format(self.name,song)

    def dance(self):
            return"{}is now dancing".format(self.name)

blu = Parrot("Blu", 10)

print(blu.sing("'Happy'"))
print(blu.dance())