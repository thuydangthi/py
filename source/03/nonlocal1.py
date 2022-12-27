# outside function 
def outer():
    x = "John"

    # nested function
    def inner():
        x = "hello"

    inner()
    return x

print(outer())
