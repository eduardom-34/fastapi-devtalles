from fastapi import FastAPI

app = FastAPI(title="Mini Blog")

@app.get("/")
def homre():
    return {'message': "Bienvenidos a Mini Blog por Cesar"}