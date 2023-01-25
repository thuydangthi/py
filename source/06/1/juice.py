from beverage import Beverage


class Juice(Beverage):
    def __init__(self, volume, fruit_content):
        super().__init__(volume=volume)
        self.__fruit_content = fruit_content

    def real_fruit(self):
        return self.__fruit_content * self.volume
