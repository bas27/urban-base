from fastapi import FastAPI

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
async def read_current_user(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def read_user(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
