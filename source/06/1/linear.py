class Linear:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __get_a(self):
        return self.__a

    def __get_b(self):
        return self.__b

    a = property(fget=__get_a)
    b = property(fget=__get_b)

    def f(self, x):
        return self.a * x + self.b
