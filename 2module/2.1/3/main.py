from fastapi import FastAPI
from pydantic import BaseModel  
# Импортируем BaseModel для валидации входных данных

app = FastAPI()

# Определяем модель данных для входных параметров
class CalculateRequest(BaseModel):
    num1: float
    num2: float
#числа будут автоматически преобразовано в float

# Определяем маршрут для POST-запросов на '/calculate'
@app.post("/calculate")
def calculate(data: CalculateRequest):
    result = data.num1 + data.num2
    
    return {"result": result}

#запуск приложения напрямую через Python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="127.0.0.1", #сервер будет доступен только локально
        port=8000, #сервер будет слушать порт 8000
        log_level="info", #уровень логирования
        reload=True #включает режим перезагрузки при изменении кода
    )
    