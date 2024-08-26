x = "Я в области видимости функции test_function"


def test_function():
    def inner_function(value="Привет"):
        print(value)
    inner_function(x)



# inner_function()
test_function()