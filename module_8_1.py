def add_everything_up(a, b):
    try:
        return round(a + b, 3)

    except TypeError:
        if isinstance(a, str) and isinstance(b, str):
            return a + b
        elif isinstance(a, str) and (isinstance(b, int) or isinstance(b, float)):
            return a + str(b)
        elif isinstance(b, str) and (isinstance(a, int) or isinstance(a, float)):
            return str(a) + b
        else:
            return "Error: types cannot be added"


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))