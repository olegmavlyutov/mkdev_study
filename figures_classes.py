# импортируем число Пи и расчет корня из библиотеки math
from math import pi, sqrt


# класс Figure с атрибутами color и side принимает параметры цвета и размера стороны (радиуса) геометрических фигур
class Figure:
    def __init__(self, color, side):
        self.color = color
        self.side = side


# классы Square, Circle и Triangle наследуют атрибуты родительского класса Figure и считают площадь встроенными методами
class Square(Figure):
    def square(self, side):
        return side ** 2

    @staticmethod
    def description(desc):
        print(desc)
        return desc

    @property
    def perimeter(self):
        return self.side * 4


class Circle(Figure):
    def square(self, side):
        return pi * side ** 2

    @staticmethod
    def description(desc):
        print(desc)
        return desc

    @property
    def perimeter(self):
        return 2 * pi * self.side


class Triangle(Figure):
    def square(self, side):
        return sqrt(3) / 4 * side ** 2

    @staticmethod
    def description(desc):
        print(desc)
        return desc

    @property
    def perimeter(self):
        return 3 * self.side


# создадим три фигуры из классов Square, Circle и Figure
first_figure = Square("red", 20)
second_figure = Circle("orange", 15)
third_figure = Triangle("yellow", 30)

# выведем информацию о фигурах и их атрибутах
Square.description("Square's description")
print("First figure, perimeter:", first_figure.perimeter)
Circle.description("Circle's description")
print("Second figure, perimeter:", second_figure.perimeter)
Triangle.description("Triangle's description")
print("Third figure, perimeter:", third_figure.perimeter)

# вывод площади фигур через методы, встроенные в классы каждой фигуры
print(first_figure.square(side=first_figure.side))
print(second_figure.square(side=second_figure.side))
print(third_figure.square(side=third_figure.side))
