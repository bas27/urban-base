from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    id: int = Field(..., ge=1, title='Enter user id', description='ID of the user')
    username: str = Field(..., min_length=5, max_length=20, title='Enter username', examples=['UrbanUser'], description='Username of the user', )
    age: int = Field(..., ge=18, le=100, title='Enter age', examples=['24'])


users: List[User] = []


def validate_user(username: str):
    if username.lower() in (u.username.lower() for u in users):
        raise HTTPException(status_code=400, detail='User with this username already exists')
    return True


@app.get('/users', response_model=List[User])
async def get_users():
    return users


@app.post('/user/{username}/{age}', response_model=User)
async def create_user(username: str, age: int):
    if validate_user(username):
        new_id = max((u.id for u in users), default=0) + 1
        new_user = User(id=new_id, username=username, age=age)
        users.append(new_user)
        return new_user


@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id: int, username: str, age: int):
    if validate_user(username):
        for user_ in users:
            if user_.id == user_id:
                user_.username = username
                user_.age = age
                return user_
        raise HTTPException(status_code=404, detail=f"User was not found")


@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id: int):
    for user_ in users:
        if user_.id == user_id:
            users.remove(user_)
            return user_
    raise HTTPException(status_code=404, detail=f"User was not found")
