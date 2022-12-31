# outside function 
def outer():
    x = "John"

    # nested function
    def inner():
        x = "hello"
        print(x)

    inner()
    return x

print(outer())
