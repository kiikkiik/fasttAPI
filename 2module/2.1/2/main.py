from fastapi import FastAPI
from fastapi.responses import HTMLResponse

#основной объект, который будет обрабатывать все входящие запрос
app = FastAPI()

#@app.get("/")-указывает, что эта функция будет вызываться при GET-запросе на корневой URL
#response_class=HTMLResponse-указывает, что ответ будет в формате HTML (а не JSON)
@app.get("/", response_class=HTMLResponse)
def read_index():
    #Читаем HTML из файла в той же папке

    #with-автоматически закрывает файл после завершения работы
    with open("index.html", "r", encoding="utf-8") as f:
        #f.read()-читает всё содержимое файла и сохраняет в переменную
        html_content = f.read()
    #Возвращаем объект ответа в формате HTML
    #content-содержимое страницы (текст из файла)
    #status_code-HTTP статус код (200 = успешный ответ)
    return HTMLResponse(content=html_content, status_code=200)