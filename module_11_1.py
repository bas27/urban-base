import requests


def get_episodes(url_api):
    episodes = []
    response = requests.get(url_api)  # получаем ответ
    if response.status_code == 200:  # проверяем код ответа
        for page in range(1, int(response.json().get('info')['pages'])):  # создаем цикл по достпным страницам
            response = requests.get(url_api + f'?page={page}')  # получаем ответ с новой страницы
            for episode in response.json().get('results'):  # создаем цикл по эпизодам
                episodes.append(episode['name'])  # добавляем эпизоды в список
        return episodes


url = 'https://rickandmortyapi.com/api/episode'

# pprint(get_episodes(url))

import pandas as pd



titanic = pd.read_csv("titanic.csv")
# print(titanic.head())  # получим первые 5 строк
# print(titanic.tail())  # получим последние 5 строк
# titanic.info() #информацию о колонках
print(titanic.describe())  # получим статистику по колонкам

from PIL import Image


def resize_image(image_paths):
    for image_path in image_paths:
        image = Image.open(image_path)
        image.resize((800, 600))
        image = image.convert('L')
        image.save(image_path)


data = []

for image in range(1, 4):
    data.append(f'./image/img{image}.jpg')

resize_image(data)
