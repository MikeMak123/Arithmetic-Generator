import math

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        if numerator < 0 or denominator < 0:  # 禁止负分数
            raise ValueError("Negative fractions are not allowed")

        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        if num < 0:
            raise ValueError("Negative result not allowed")
        return Fraction(num, den)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __str__(self):
        if self.numerator >= self.denominator:
            whole = self.numerator // self.denominator
            remainder = self.numerator % self.denominator
            return f"{whole}'{remainder}/{self.denominator}" if remainder else str(whole)
        return f"{self.numerator}/{self.denominator}"