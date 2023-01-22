class Student:
    """
    Student class
    """
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_age(self, age: int):
        if age > 0:
            self.__age = age

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name.title()

    def __str__(self):
        return f'{self.__name} {self.__age}'

s1 = Student('tom', 10)
print(s1)
s1.set_name('bim bim')
print(s1)
s1.set_age(22)
print(s1)
s1.set_age(-1)
print(s1)
print(help(s1))
