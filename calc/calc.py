import tkinter as tk


def get_values():
    num1 = int(number_1.get())
    num2 = int(number_2.get())
    return num1, num2


def insert_values(value):
    answer.delete(0, 'end')
    answer.insert(0, value)


def add():
    num1, num2 = get_values()
    result = num1 + num2
    insert_values(result)


def minus():
    num1, num2 = get_values()
    result = num1 - num2
    insert_values(result)


def multiply():
    num1, num2 = get_values()
    result = num1 * num2
    insert_values(result)


def div():
    num1, num2 = get_values()
    result = num1 / num2
    insert_values(result)


window = tk.Tk()
window.title("Calculator")
window.geometry("400x400")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=4, height=2, command=add)
button_add.place(x=100, y=300)
button_minus = tk.Button(window, text="-", width=4, height=2, command=minus)
button_minus.place(x=150, y=300)
button_multiply = tk.Button(window, text="x", width=4, height=2, command=multiply)
button_multiply.place(x=200, y=300)
button_del = tk.Button(window, text="/", width=4, height=2, command=div)
button_del.place(x=250, y=300)
number_1 = tk.Entry(window, width=25)
number_1.place(x=100, y=75)
number_2 = tk.Entry(window, width=25)
number_2.place(x=100, y=125)
answer = tk.Entry(window, width=25)
answer.place(x=100, y=190)

number_1_label = tk.Label(window, text="Введите первое число:")
number_2_label = tk.Label(window, text="Введите второе число:")
answer_label = tk.Label(window, text="Результат:")
number_1_label.place(x=100, y=45)
number_2_label.place(x=100, y=99)
answer_label.place(x=100, y=160)
window.mainloop()
