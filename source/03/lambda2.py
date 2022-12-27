def multi_func(n):
    return lambda a : a * n

doubler = multi_func(2)
tripler = multi_func(3)

print(doubler(11))
print(tripler(11))
