import math
class Shape:
    def area(self, width, height):
        return width * height  # Делает площадь только для прямоугольника


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Прямоугольник площадью {super().area(self.width, self.height)}'

class Circle(Shape):
    def __init__(self, r)->None:
        self.radius = r
    def area(self) -> float:
        return self.radius*2*math.pi

    def __str__(self):
        return f'Круг площадью {self.area()}'

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
    def __str__(self):
        return f'Я квадрат моя площадь {super().area(self.side, self.side)}'
