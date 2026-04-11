from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

# Определяем модель данных для создания пользователя
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None
    is_subscribed: Optional[bool] = None
    
    # Добавляем валидацию для возраста
    @classmethod
    def validate_age(cls, v):
        if v is not None and v <= 0:
            raise ValueError('Age must be a positive integer')
        return v

# Определяем маршрут POST для создания пользователя
@app.post("/create_user")
def create_user(user: UserCreate):


    return user.model_dump()