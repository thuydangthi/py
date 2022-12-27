# outside function 
def outer():
    x = "John"

    # declare nonlocal variable
    def inner():
        nonlocal x
        x = "hello"

    inner()
    return x

print(outer())
