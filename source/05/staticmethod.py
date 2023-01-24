class User:
    count = 0
    def __init__(self, fname='', lname='', age=18):
        self.fname = fname
        self.lname = lname
        self.age = age
        User.count += 1

    def print(self):
        print(f'{self.fname} {self.lname} ({self.age} years old)')

    @property
    def full_name(self):
        return f'{self.fname} {self.lname}'

    @classmethod
    def print_count(cls):
        print(f'{cls.count} objects created')

    @staticmethod
    def birth_year(age: int) -> int:
        from datetime import datetime as dt
        year = dt.now().year
        return year - age


if __name__ == '__main__':
    trump = User('Donald', 'Trump', 22)
    trump.print()
    print(trump.full_name)
    print(User.count)
    User.print_count()
    print(trump.birth_year(37))
