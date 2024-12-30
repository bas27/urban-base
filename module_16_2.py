from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
async def root():
    """
    Главная страница
    :return:
    """
    return "Главная страница"


@app.get("/user/admin")
async def admin():
    """
    Страница администратора
    :return:
    """
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def read_current_user(user_id: Annotated[int, Path(ge=1, le=100, title='Enter User ID', example='1')]):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
async def read_user(
        username: Annotated[str, Path(min_length=5, max_length=20, title='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, title='Enter age', example='24')]):
    """
    Страница пользователя
    :param username: Имя пользователя
    :param age: Возраст пользователя
    :return:
    """
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
