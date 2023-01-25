class Beverage:
    def __init__(self, volume):
        self.volume = volume

    def __set_volume(self, volume):
        self.__volume = volume

    def __get_volume(self):
        return self.__volume

    volume = property(fget=__get_volume, fset=__set_volume)
