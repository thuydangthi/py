def myfunc(n):
    return abs(n - 50)

nums = [100, 50, 65, 82, 23]
nums.sort(key = myfunc, reverse=True)
print(nums)
