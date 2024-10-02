import itertools
import math


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=False):
        self.__sides = sides
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        custom_color = [r, g, b]
        if len(custom_color) == 3:
            for i in custom_color:
                if i < 0 or i > 255:
                    return False
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def __is_valid_sides(self, *new_sides):
        if len([*new_sides]) == self.sides_count:
            for side in new_sides:
                if side > 0:
                    return True
        else:
            return False

    def get_sides(self):
        return [self.__sides]

    def __len__(self):
        return self.sides_count * self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            if len(new_sides) == 1:
                self.__sides = new_sides[0]
            else:
                for side in new_sides:
                    self.__sides.append(side)


class Circle(Figure):
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.sides_count = 1
        self.__radius = sides / 2 * math.pi

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.sides_count = 3
        self.semi_perimeter = sum(sides) / 2

    def get_square(self):
        return math.sqrt(
            self.semi_perimeter * (self.semi_perimeter - self.sides[0]) * (self.semi_perimeter - self.sides[1]) * (
                        self.semi_perimeter - self.sides[2]))


class Cube(Figure):
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.sides_count = 12
        if len([sides]) == 1:
            self.__sides = [i for i in itertools.repeat(sides, 12)]
        else:
            self.__sides = [i for i in itertools.repeat(1, 12)]
        print(self.__sides)

    def get_volume(self):
        return self.__sides[0] ** 3

    pass


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_sides())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится

# circle1.set_sides(15) # Изменится
# print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
# print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
