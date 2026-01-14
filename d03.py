import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def deagonal(self):
        return self.side * math.sqrt(2)


square1 = Square(side=1.5)
print(f"{square1.area():.2f}")  # 2.25
print(f"{square1.deagonal():.2f}")  # 2.12


square2 = Square(side=15)
print(square2.area())  # 225
print(f"{square2.deagonal():.2f}")  # 21.21
