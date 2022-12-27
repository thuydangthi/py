# declare variable x
x = 2

def mmath():
    # use of global keyword
    global x

    x *= 2
    print("Inside mmath function ", x)

print("Before calling mmath function ", x)
mmath()
print("After calling mmath function ", x)
