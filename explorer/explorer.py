import tkinter
import os
from tkinter import filedialog


def open_file():
    filename = filedialog.askopenfilename(initialdir='./', title='Выберите файл',
                                          filetypes=(('txt files', '*.txt'),
                                                     ('all files', '*.*'))
                                          )

    text['text'] = text['text'] + ' ' + filename
    os.startfile(filename)

window = tkinter.Tk()
window.title('Проводник')
window.geometry('400x180')
window.configure(bg='black')
window.resizable(False, False)
text = tkinter.Label(window, text='Файл', background='blue', fg='white', height=5, width=50)
text.grid(row=1, column=1)
button_select = tkinter.Button(window, height=2, width=20, bg='green', fg='white', text='Выбрать файл',
                               command=open_file)
button_select.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()

