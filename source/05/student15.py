class Student:
    count = 0

    def __init__(self, name, house):
        self.name = name
        self.house = house
        Student.count += 1
    
    def attendance(self):
        print(f"{self.name} is here!")

    @classmethod
    def show_count(cls):
        print(cls.count)


student1 = Student("Lan", "Gryffindor")
student1.show_count()
student2 = Student("Tuan", "Gryffindor")
student2.show_count()
Student.show_count()
