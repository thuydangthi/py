foods = ["apple", "banana", "cherry"]

new_foods = list(foods)
print(new_foods)

foods[1] = "cherry"
print(new_foods)

new_foods.pop()
print(foods)
