class Student:
    grade = 10
    name = "Penguin"
    
    def introduction(self):
        print("Hi! I am a student,")
        print("A Student in Codingal")

    def details(self):
        print("My name is", self.name)
        print("I study in grade", self.grade)

ob = Student()
ob.introduction()
ob.details()