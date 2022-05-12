class Person:

    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.__pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.__pay *= (1.0 + percent)

    def __str__(self):
        return f'Person name:{self.name}, age:{self.age}, job:{self.job}'


class Manager(Person):

    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')


bob = Person('Bob Smith', 44)
sue = Person('Sue Jones', 47, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)

print(bob)
print(sue)
print(tom)

