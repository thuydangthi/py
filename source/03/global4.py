# create a function:
def myfunction():
    global x
    x = "hello"

# execute the function:
myfunction()

# x should now be global, and accessible in the global scope.
print(x)
