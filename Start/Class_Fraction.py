import math


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        gcd = math.gcd(newnum, newden)
        return Fraction(newnum // gcd, newden // gcd)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        gcd = math.gcd(newnum, newden)
        return Fraction(newnum // gcd, newden // gcd)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        gcd = math.gcd(newnum, newden)
        return Fraction(newnum // gcd, newden // gcd)

    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        gcd = math.gcd(newnum, newden)
        return Fraction(newnum // gcd, newden // gcd)

    def __lt__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        gcd = math.gcd(newnum, newden)
        return Fraction(newnum // gcd, newden // gcd)

    def __eq__(self, otherfraction):
        if (self.num / self.den) == (otherfraction.num / otherfraction.den):
            return True
        else:
            return False

    def __ne__(self, otherfraction):
        if (self.num / self.den) != (otherfraction.num / otherfraction.den):
            return True
        else:
            return False

    def __lt__(self, otherfraction):
        if (self.num / self.den) < (otherfraction.num / otherfraction.den):
            return True
        else:
            return False

    def __gt__(self, otherfraction):
        if (self.num / self.den) > (otherfraction.num / otherfraction.den):
            return True
        else:
            return False

    def __le__(self, otherfraction):
        if (self.num / self.den) <= (otherfraction.num / otherfraction.den):
            return True
        else:
            return False

    def __ge__(self, otherfraction):
        if (self.num / self.den) >= (otherfraction.num / otherfraction.den):
            return True
        else:
            return False


f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
f3 = f1 + f2
print(f1 <= f2)
print(f3)
