# outside function 
def outer():
    x = "John"

    # declare nonlocal variable
    def inner():
        nonlocal x
        x = "hello"
        print(x)

    inner()
    return x

print(outer())
