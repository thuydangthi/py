l = [1, 2, 3]
t = ('xin chao', l, True)
check_t = l in t

print(check_t)
print(l in t)
print(l not in t)

if l in t:
    print("Y")

if 4 not in l:
    print("N")
