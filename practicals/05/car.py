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
        1 km ~ 1 fuel
        """
        if distance <= 1*self.fuel:
            self.fuel -= distance
            return distance
        else:
            self.fuel = 0
            return 1*self.fuel


car1 = Car(name="oto")

print(f"{car1.name} - {car1.fuel}")
car1.add_fuel(50)
print(f"{car1.name} - {car1.fuel}")
print(car1.drive(25))
print(f"{car1.name} - {car1.fuel}")
print(car1.drive(30))
print(f"{car1.name} - {car1.fuel}")
