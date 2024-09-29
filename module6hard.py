class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled):
        self.__sides = sides
        self.__color = color
        self.filled = filled


class Circle(Figure):
    pass


class Triangle(Figure):
    pass


class Cube(Figure):
    pass
