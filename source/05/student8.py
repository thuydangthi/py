class Student:
    def __init__(self, name="Default name", house="Default house"):
        self.name = name
        self.house = house

student1 = Student()
print(f"{student1.name} from {student1.house}")

student2 = Student("Anna", "Gryffindor")
print(f"{student2.name} from {student2.house}")
