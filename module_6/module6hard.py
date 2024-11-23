import math
import itertools


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=True):
        self.__sides = [side for side in sides]
        self.__color = [color for color in color]
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        for side in sides:
            if side > 0 and len(sides) == self.sides_count:
                continue
            else:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.sides_count == len(new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        if len(sides) != self.sides_count:
            self.set_sides(1)
        self.__radius = sides[0] / 2 * math.pi


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        if len(sides) != self.sides_count and len(sides) != 1:
            self.set_sides(1, 1, 1)
        elif len(sides) == 1:
            self.set_sides(sides[0], sides[0], sides[0])

    def get_square(self):
        sides = self.get_sides()
        semi_perimeter = sum(sides) / 2
        square = math.sqrt(abs(semi_perimeter * (semi_perimeter - sides[0]) * (semi_perimeter - sides[1]) *
                               (semi_perimeter - sides[2])))
        return f'{square:.2f}'


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        Figure.__init__(self, color, sides)
        if len(sides) != self.sides_count and len(sides) != 1:
            sides = [i for i in itertools.repeat(1, 12)]
            self.set_sides(*sides)
        elif len(sides) == 1:
            sides = [i for i in itertools.repeat(sides[0], 12)]
            self.set_sides(*sides)

    def get_volume(self):
        sides = self.get_sides()
        volume = sides[0] ** 3
        return f'{volume:.2f}'


# circle1 = Circle((200, 200, 100), 10)
# circle2 = Circle((200, 200, 100), 10, 15, 6)
# circle1.set_color(55, 66, 77)
# print(circle1.get_color())
# print(circle1.get_sides())
# print(circle2.get_sides())
# circle1.set_sides(15)
# print(circle1.get_sides())
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
# ======================
# triangle1 = Triangle((212, 40, 155), 9, 55, 66)
# triangle2 = Triangle((200, 200, 100), 10, 6)
# triangle3 = Triangle((200, 200, 100), 23)
# triangle1.set_color(55, 66, 77)
# print(triangle1.get_color())
# triangle1.set_sides(15, 15, 15)
# print(triangle1.get_sides())
# print(triangle1.get_square())
# print(triangle2.get_sides())
# print(triangle3.get_sides())
# print(triangle3.get_square())
# print(len(triangle3))
# =========================
# cube1 = Cube((200, 200, 100), 9, 12)
# print(cube1.get_sides())

# Проверка на изменение цветов:
# cube1 = Cube((222, 35, 130), 6)
# cube1.set_color(300, 70, 15)  # Не изменится
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
#
# # Проверка объёма (куба):
# print(cube1.get_volume())
