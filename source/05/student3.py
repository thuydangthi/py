class Student:
    ...


student1 = Student()
student1.name = input("Name: ")
student1.house = input("House: ")
print(f"{student1.name} from {student1.house}")

student2 = Student()
print(f"{student2.name} from {student2.house}")
