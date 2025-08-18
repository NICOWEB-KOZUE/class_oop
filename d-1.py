import math


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        # 面積 = π × r^2
        area = math.pi * (self.radius**2)
        return round(area,  2)

    def perimeter(self) -> float:
        # 周囲長(=円周の長さ) = 2 × π × r
        perimeter = 2 * math.pi * self.radius
        return round(perimeter, 2)


# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85
