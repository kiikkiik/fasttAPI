from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Feedback(BaseModel):
    name: str
    message: str

#список для хранения всех отзывов
feedbacks = []

#определяем маршрут POST для получения отзывов
@app.post("/feedback")
def create_feedback(feedback: Feedback):
    
    #сохраняем отзыв в список
    feedbacks.append(feedback)
    
    return {
        "message": f"Feedback received. Thank you, {feedback.name}."
    }