import math

class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled=False):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self):
        if 0 <= self.__color[0] <= 255 and \
                0 <= self.__color[1] <= 255 and \
                0 <= self.__color[2] <= 255:
            return True
        else:
            return False

    def set_color(self, color):
        if self.__is_valid_color():
            self.__color = color
        else:
            print("Invalid color")

    def __is_valid_sides(self, *sides):
        if self.__sides > 0 and sides.count(*sides) == self.sides_count:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return self.sides_count * self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides():
            self.__sides = new_sides


class Circle(Figure):
    def __init__(self, sides, color):
        super().__init__(sides, color)
        self.sides_count = 1
        self.__radius = sides / 2 * math.pi

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)
        self.sides_count = 3
        self.semi_perimeter = sum(sides) / 2

    def get_square(self):
        return math.sqrt(self.semi_perimeter * (self.semi_perimeter - self.sides[0]) * (self.semi_perimeter - self.sides[1]) * (self.semi_perimeter - self.sides[2]))


class Cube(Figure):
    pass


circle1 = Circle((200, 200, 100), 10)
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())