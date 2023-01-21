"""Car class"""


class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0, name=""):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.fuel = fuel
        self.odometer = 0
        self.name = name

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        # TODO

car1 = Car()

# car1.add_fuel
# car1.drive
# print(car1.distance)
