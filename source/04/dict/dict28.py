car1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car2 = car1.copy()
print(car2)

car1["year"] = 2022
print(car2["year"])

car2["color"] = "black"
print(car1["color"]) # error KeyError: 'color'
