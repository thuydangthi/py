class Student:
    count = 0

    def __init__(self, name, house, age):
        self.name = name
        self.house = house
        self.age = age
        Student.count += 1

    def attendance(self):
        print(f"{self.name} is here!")

    def __str__(self):
        return f"{self.name} is {self.age}"


student1 = Student("Lan", "Gryffindor", "hhh")
print(student1)
