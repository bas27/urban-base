from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Alex, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20,
                                      regex="^[a-zA-Z_-]+$", title='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=100, title='Enter age', example='24')]
):
    new_id = int(max(users.keys())) + 1 if len(users) > 0 else 1
    users[str(new_id)] = f'Имя: {username}, возраст: {age}'
    return f"User {new_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=1, title='Enter user id', example='1')],
        username: Annotated[str, Path(min_length=5, max_length=20,
                                      regex="^[a-zA-Z_-]+$", title='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=100, title='Enter age', example='24')]):
    if str(user_id) not in users.keys():
        return f"User {user_id} not found"
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is updated"


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, title='Enter user id', example='1')]):
    if str(user_id) not in users.keys():
        return f"User {user_id} not found"
    del users[str(user_id)]
    return f"The user {user_id} is deleted"
