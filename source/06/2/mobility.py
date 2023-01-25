class Car:
    def __init__(self, max_speed):
        self.__max_speed = max_speed

    def __get_max_speed(self):
        return self.__max_speed

    def __set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    max_speed = property(fget=__get_max_speed, fset=__set_max_speed)


c = Car(10)
print(c.max_speed)


class ElectricCar(Car):
    def __init__(self, max_speed, energy_storage, consumption, t_charge):
        super().__init__(max_speed)
        self.__energy_storage = energy_storage
        self.__consumption = consumption
        self.__t_charge = t_charge

    def range_limit(self):
        return self.__energy_storage * 100

    def travel_time(self, distancec):
        ...
