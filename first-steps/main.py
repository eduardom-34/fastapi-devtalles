from email.policy import default
from turtle import pos
from fastapi import FastAPI, Query

app = FastAPI(title="Mini Blog")


BLOG_POST = [
    {"id": 1, "title": "Hola desde FastAPI", "Content": "Este es mi primer post con FastAPI"},
    {"id": 2, "title": "Mi segundo Post con FastAPI", "Content": "Este es mi segundo post con FastAPI"},
    {"id": 3, "title": "Django vs FastAPI", "Content": "FastAPI es mas rapido por x razon"},
]

@app.get("/")
def home():
    return {'message': "Bienvenidos a Mini Blog por Cesar"}


@app.get("/posts")
def list_posts(query: str | None = Query(default=None, description="Texto para buscar por titulo")):
    
    if query:
        results = [post for post in BLOG_POST if query.lower() in post["title"].lower()]
        # for post in BLOG_POST:
        #     if query.lower() in post["title"].lower():
        #         results.append(post)
                
        return {"data": results, "query": query}
    
    return {"data": BLOG_POST}

