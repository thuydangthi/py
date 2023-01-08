car1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car2 = car1
print(car2["year"])

car1["year"] = 2022
print(car2["year"])

car2["color"] = "black"
print(car1["color"])
