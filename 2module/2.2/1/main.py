from fastapi import FastAPI
from models import User

app = FastAPI()

# Создаем экземпляр модели User с указанными значениями
user = User(name="John Doe", id=1)

# Определяем маршрут для GET-запросов на '/users'
@app.get("/users")
def get_user():  #функция возвращает данные пользователя в формате JSON
    return user.dict()

#http://127.0.0.1:8000/users