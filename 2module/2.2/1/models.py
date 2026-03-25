from pydantic import BaseModel

# Определяем модель пользователя с полями name (строка) и id (целое число)
class User(BaseModel):
    name: str
    id: int