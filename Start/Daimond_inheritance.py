class A:
    def hi(self):
        print("A")


class B(A):
    def hi(self):
        print("B")


class C(A):
    def hi(self):
        print("C")


class D(B, C):
    pass


print(D.mro()) #В Python3 можно посмотреть в каком порядке будут проинспектированы родительские классы при помощи метода класса mro():

d = D()
d.hi()
