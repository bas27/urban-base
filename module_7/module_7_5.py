import os
import time
from os.path import join, getsize, getmtime, dirname

for root, dirs, files in os.walk('../module_6'):
    for file in files:
        filepath = join(root, file)
        filetime = getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = getsize(filepath)
        parent_dir = dirname(root)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
