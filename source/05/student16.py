class Student:
    def __init__(self):
        self.__private = False

s = Student()

# shouldn't do it like this
s.__private = True
print(s.__private)
