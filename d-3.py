import math


class Square:
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        # 　正方形の面積 = 一辺　 × 一辺
        area = self.side ** 2
        return round(area, 2)

    def diagonal(self) -> float:
        # 　対角線 = √(辺² + 辺²)
        diagonal = math.sqrt(self.side ** 2 + self.side ** 2)
        return round(diagonal, 2)


# 半径1.5の正方形
square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

# 半径15の正方形
square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
