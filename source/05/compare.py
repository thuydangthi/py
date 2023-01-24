class MyClass:

    def instancemethod(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


obj1 = MyClass()

print(obj1.instancemethod())
# MyClass.instancemethod() # error MyClass.instancemethod() missing 1 required positional argument: 'self'

print(MyClass.classmethod())
print(obj1.classmethod())

print(MyClass.staticmethod())
print(obj1.staticmethod())
