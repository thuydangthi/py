# declare variable x
x = 2

def mmath():
    # try to change the value of x in mmath function
    x *= 2
    print(x)

mmath() # cannot access local variable 'x' where it is not associated with a value
