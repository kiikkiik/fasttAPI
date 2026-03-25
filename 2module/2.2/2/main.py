from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

# Определяем маршрут для POST-запросов на '/user'
@app.post("/user")
def create_user(user: User):

    is_adult = user.age >= 18
    
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }