class Student:
    count = 0

    def __init__(self, name="Default name", house="Default house"):
        self.name = name
        self.house = house
        Student.count += 1

student1 = Student()
print(Student.count, student1.count)
student2 = Student()
print(Student.count, student2.count)
student3 = Student()
print(Student.count, student3.count)
