class Student:
    def __init__(self, name="Default name", house="Default house"):
        self.name = name
        self.house = house

student1 = Student()
print(f"{student1.name} from {student1.house}")
student1.name = "Anna"
print(f"{student1.name} from {student1.house}")
