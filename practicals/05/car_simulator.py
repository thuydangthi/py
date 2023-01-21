"""
Create a car driving simulator in car_simulator.py that uses the Car class that works like the following sample output...

Note: Please do this (and every problem of significant size) incrementally:

Start by just testing one method call,
then another,
then write the menu and put it all together.
(Do not start with the menu.)
Remember to use the class's functionality - don't rewrite anything you've already got.

Do you remember how to construct a simple menu-driven program? If not, it's very important that you revise earlier lectures and practicals (it was in prac 1).
You will need to import the car module, create a Car object, and use appropriate methods on that object.

Let's drive!
Enter your car name: The bomb
The bomb, fuel=100, odo=0
Menu:
d) drive
r) refuel
q) quit
Enter your choice: f
Invalid choice

The bomb, fuel=100, odo=0
Menu:
d) drive
r) refuel
q) quit
Enter your choice: d
How many km do you wish to drive? 39
The car drove 39km.

The bomb, fuel=61, odo=39
Menu:
d) drive
r) refuel
q) quit
Enter your choice: d
How many km do you wish to drive? -25
Distance must be >= 0
How many km do you wish to drive? 100
The car drove 61km and ran out of fuel.

The bomb, fuel=0, odo=100
Menu:
d) drive
r) refuel
q) quit
Enter your choice: r
How many units of fuel do you want to add to the car? -80
Fuel amount must be >= 0
How many units of fuel do you want to add to the car? 120
Added 120 units of fuel.

The bomb, fuel=120, odo=100
Menu:
d) drive
r) refuel
q) quit
Enter your choice: d
How many km do you wish to drive? 25
The car drove 25km.

The bomb, fuel=95, odo=125
Menu:
d) drive
r) refuel
q) quit
Enter your choice: q

Good bye The bomb's driver.

"""