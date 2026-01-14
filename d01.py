import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi

    def perimeter(self):
        return 2 * self.radius * math.pi


# 半径1の円
circle1 = Circle(radius=1)
print(f"{circle1.area():.2f}")  # 3.14
print(f"{circle1.perimeter():.2f}")  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(f"{circle3.area():.2f}")  # 28.27
print(f"{circle3.perimeter():.2f}")  # 18.85
