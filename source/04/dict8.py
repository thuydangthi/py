car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x) # before the change

car["year"] = 2020

print(x) #a fter the change
