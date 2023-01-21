class Student:
    def __init__(self, name="Default name", house="Default house"):
        self.name = name
        self.house = house

student1 = Student()
print(f"{student1.name} from {student1.house}")

student2 = Student("Anna", "Gryffindor")
print(f"{student2.name} from {student2.house}")

student1.age = 11
print(f"Age of student 1: {student1.age}")
