class Student:
    count = 0

    def __init__(self, name, house):
        self.name = name
        self.house = house
        Student.count += 1
    
def attendance(name):
    print(f"{name} is here!")

student1 = Student("Lan", "Gryffindor")
student1.check = attendance
student1.check(student1.name)
student2 = Student("Minh", "Gryffindor")
student2.check(student2.name)
