class User:
    count = 0

    def __init__(self, name="Thuy", age=12, cccd="8768275628", is_active=True):
        self.name = name
        self.age = age
        self.cccd = cccd
        self.is_active = is_active
        User.count += 1

    def login(self):
        if not self.is_active:
            print("Login fail")
        else:
            print("Hello")



u1 = User(name="Chi")
# u1.login()

u2 = User(is_active=False)
# u2.login()
