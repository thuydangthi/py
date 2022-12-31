l = [1,3,4,6,7,9,12,11]

# c1

new_l = []

for i in l:
    if i % 2 == 0:
        new_l.append(i)

print(new_l)

# c2

new_l = list(filter(lambda i: (i%2 == 0), l))
print(new_l)
