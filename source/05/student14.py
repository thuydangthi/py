class Student:
    count = 0

    def __init__(self, name, house):
        self.name = name
        self.house = house
        Student.count += 1
    
    def attendance(self):
        print(f"{self.name} is here!")


student1 = Student("Lan", "Gryffindor")
student1.attendance()
student2 = Student("Tuan", "Gryffindor")
student2.attendance()
