class Parent:
    count = 0
    def __init__(self):
        self._protected = True
        self.__private = True

class Child(Parent):
    ...

c1 = Child()
print(c1._protected) # True
print(c1.__private) # 'Child' object has no attribute '__private'
