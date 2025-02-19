from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

users = [
    User(id=1, name="Tiago", email="tiago@api.com"),
    User(id=2, name="Bona", email ="bona@api.com")
]

@app.get("/users", response_model=List[User]) ##usar response model garante que o dados vao do jeito correto 
##FastApi faz a conversão corretamente
def get_users():
     return users

@app.post("/users", response_model=User)
def create_user(user: User):
    users.append(user) #coloca o novo usuario na lista
    return user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error":"Não existe esse usuario"}


