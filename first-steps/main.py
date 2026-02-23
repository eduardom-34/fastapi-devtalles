
from email.policy import HTTP
from math import ceil
from re import search
import string
from turtle import pos
from fastapi import Body, FastAPI, Query, HTTPException, Path
from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Literal, Optional, List, Union

app = FastAPI(title="Mini Blog")


BLOG_POST = [
    {"id": 1, "title": "Hola desde FastAPI", "content": "Este es mi primer post con FastAPI"},
    {"id": 2, "title": "Mi segundo Post con FastAPI", "content": "Este es mi segundo post con FastAPI"},
    {"id": 3, "title": "Django vs FastAPI", "content": "FastAPI es mas rapido por x razon", 
     "tags": [
         {"name": "django"}, 
         {"name": "python"},
         {"name": "fastapi"}
         ]},
    {"id": 4, "title": "Hola desde FastAPI", "content": "Este es mi primer post con FastAPI"},
    {"id": 5, "title": "Mi segundo Post con FastAPI", "content": "Este es mi segundo post con FastAPI"},
    {"id": 6, "title": "Django vs FastAPI", "content": "FastAPI es mas rapido por x razon"},
    {"id": 7, "title": "Hola desde FastAPI", "content": "Este es mi primer post con FastAPI"},
    {"id": 8, "title": "Mi segundo Post con FastAPI", "content": "Este es mi segundo post con FastAPI"},
    {"id": 9, "title": "Django vs FastAPI", "content": "FastAPI es mas rapido por x razon"},
    {"id": 10, "title": "Hola desde FastAPI", "content": "Este es mi primer post con FastAPI"},
    {"id": 11, "title": "Mi segundo Post con FastAPI", "content": "Este es mi segundo post con FastAPI"},
    {"id": 12, "title": "Django vs FastAPI", "content": "FastAPI es mas rapido por x razon"},
    {"id": 13, "title": "Hola desde FastAPI", "content": "Este es mi primer post con FastAPI"},
    {"id": 14, "title": "Mi segundo Post con FastAPI", "content": "Este es mi segundo post con FastAPI"},
    {"id": 15, "title": "Django vs FastAPI", "content": "FastAPI es mas rapido por x razon"},
    {"id": 16, "title": "Hola desde FastAPI", "content": "Este es mi primer post con FastAPI"},
    {"id": 17, "title": "Mi segundo Post con FastAPI", "content": "Este es mi segundo post con FastAPI"},
    {"id": 18, "title": "Django vs FastAPI", "content": "FastAPI es mas rapido por x razon"},
]

class Tag(BaseModel):
    name: str = Field(..., min_length=2, max_length=30, description="Nombre de la etiqueta")
    
class Author(BaseModel):
    name: str
    email: EmailStr

class PostBase(BaseModel):
    title: str
    content: str
    tags: Optional[List[Tag]] = Field(default_factory=list) #esto crea una lista vacoa por cada objeto 
    author: Optional[Author] = None
    
class PostCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Titulo del post (minimo 3 caracteres, maximo 100)",
        examples=["Mi primer post con FastAPI"]
    )
    content: str = Field(
        default="Contenido no disponible",
        min_length=10,
        description="Contenido del post (min 10 caracteres)",
        examples=["Este es un contenido valido porque tiene 10 caracteres o mas"]
    )
    tags: List[Tag] = Field(default_factory=list)  #[]
    author: Optional[Author] = None
    
    @field_validator("title")
    @classmethod
    def not_allowed_title(cls, value:str) -> str:
        if "spam" in value.lower():
            raise ValueError("El titulo no puede contener la palbra: 'spam")
        return value

class PostUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    content: Optional[str] = None
    
class PostPublic(PostBase):
    id: int
    
    
class PostSummary(BaseModel):
    id: int
    title: str

class PaginatedPost(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    has_prev: bool
    has_next: bool
    order_by: Literal["id", "title"]
    direction: Literal["asc", "desc"]
    search: Optional[str] = None
    items: List[PostPublic]

@app.get("/")
def home():
    return {'message': "Bienvenidos a Mini Blog por Cesar"}


@app.get("/posts", response_model=PaginatedPost)
def list_posts(
    text: Optional[str] = Query(
    default=None, 
    deprecated=True,
    description="Parametro obsoleto, usa query o search en su lugar"
),
    query: Optional[str] = Query(
    default=None, 
    description="Texto para buscar por titulo",
    alias='search',
    min_length=3,
    max_length=50,
    pattern=r"^[\w\sáéíóúÁÉÍÓÚüÜ-]+$"
),
    per_page: int = Query(
        10, ge=1, le=50,
        description="Numero de resultados 1-50"
),
    page: int = Query(
        1, ge=1,
        description="Pagina a mostrar (empezando desde 1)"
),
    
    order_by: Literal["id", "title"] = Query(
        "id", description="Campo de orden"
),
    direction: Literal["asc", "desc"] = Query(
        "asc", description="Direccion de orden"
)              
):
    
    results = BLOG_POST
    
    query = query or text
    
    
    if query:
        results =  [post for post in results if query.lower() in post["title"].lower()]
        # for post in BLOG_POST:
        #     if query.lower() in post["title"].lower():
        #         results.append(post)
        
    total = len(results)
    total_pages = ceil(total/per_page) if total > 0 else 0
    
    if total_pages == 0:
        current_page = 1
    else:
        current_page = min(page, total_pages)
    
    results = sorted(results, key=lambda  post: post[order_by], reverse=(direction=="desc"))
  
    if total_pages == 0:
        items = []
    else:
        start = (current_page - 1) * per_page
        items = results[start: start + per_page]
        
    has_prev = current_page > 1
    has_next = current_page < total_pages if total_pages > 0 else False
        
    return PaginatedPost(
        page=current_page,
        per_page=per_page,
        total=total,
        total_pages=total_pages,
        has_prev=has_prev,
        has_next=has_next,
        order_by=order_by,
        direction=direction,
        search=query,
        items=items)

@app.get("/posts/by-tags", response_model=List[PostPublic])
def filter_by_tags(
    tags: List[str] = Query(
        ...,
        min_length=2,
        description="Una o mas etiquetas. Ejemplo ?tags=python&tags=fastapi"
    )
):
    tags_lower = [tag.lower() for tag in tags]
    return [
        post for post in BLOG_POST if any( tag["name"].lower() in tags_lower for tag in post.get("tags", []))
    ]

@app.get("/posts/{post_id}", response_model=Union[PostPublic, PostSummary], response_description="Post encontrado")
def get_post(post_id: int = Path(
        ...,
        ge=1,
        title="ID del post",
        description="ID del post a obtener (debe ser un entero positivo)",
        example=1
    ), include_content: bool = Query(default=True, description="Incluir o no el contenido")):
    
    for post in BLOG_POST:
        if post["id"] == post_id:
            if not include_content:
                return {"id": post["id"], "title": post["title"]}
            return post
    
        
    return HTTPException(status_code=404, detail="Post no encontrado")


@app.post("/posts", response_model=PostPublic, response_description="Post creado (OK)")
def create_post(post: PostCreate):
    new_id = (BLOG_POST[-1]["id"] + 1) if BLOG_POST else 1
    new_post = {"id": new_id, 
                "title": post.title,
                "content": post.content, 
                "tags": [tag.model_dump() for tag in post.tags],
                "author": post.author.model_dump() if post.author else None
                }
    BLOG_POST.append(new_post)
    return new_post
        
        
@app.put("/posts/{post_id}", response_model=PostPublic, response_description="Post actualizado", response_model_exclude_none=True)
def update_post(post_id: int, data: PostUpdate):
    for post in BLOG_POST:
        if post["id"] == post_id:
            playload = data.model_dump(exclude_unset=True) #{"title": "Ricardo", "content": None} por eso usamos exlucde unset
            if "title" in playload: post["title"] = playload['title']
            if "content" in playload: post['content'] = playload['content']
            return post
        
    raise HTTPException(status_code=404, detail="Post no encontrado")
    
@app.delete("/posts/{post_id}", status_code=204)
def delete_post(post_id: int):
    for index, post in enumerate(BLOG_POST):
        if post["id"] == post_id:
            BLOG_POST.pop(index)
            return
    raise HTTPException(status_code=404, detail="Post no encontrado")