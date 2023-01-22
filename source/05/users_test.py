from users0 import User

john = User("John", "secret")

print(john._hashed_password)
print(john.password)  # error

john.password = "supersecret"
print(john._hashed_password)
