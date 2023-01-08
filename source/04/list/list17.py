foods = ["apple", "banana", "cherry"]

new_foods = foods.copy()
print(new_foods)

foods[1] = "cherry"
print(new_foods)

new_foods.pop()
print(foods)
