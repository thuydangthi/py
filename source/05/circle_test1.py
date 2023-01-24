from circle import Circle


c1 = Circle(20)
print(c1.radius)
c1.radius = 11
print(c1.radius)
print(Circle.radius.fset)
# del c1.radius
# print(c1.radius) # error
