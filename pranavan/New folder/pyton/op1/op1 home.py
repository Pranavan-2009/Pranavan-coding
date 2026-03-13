# class student:
#     grade = 11
#     print("Hi I am a student of grade",grade)

# ob = student()

class student:
    grade = 11
    name = "Raj"

    def introdution(self):
      print("Hi I am a student")

    def details(self):
        print("My name is",self.name)
        print("I study in grade",self.grade)

ob = student()
ob.introdution()
ob.details()