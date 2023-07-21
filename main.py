from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
# import uvicorn


class Todo(BaseModel):
    name: str
    due_date: str
    description: str


app = FastAPI(title="fastAPI_todo")

store_todo = []


@app.get("/")
async def home():
    return {"Message": "Redirect to /docs"}


@app.post("/todo/")
async def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo


@app.get("/todo/", response_model=List[Todo])
async def get_all_todos():
    return store_todo


@app.get("/todo/{id}")
async def get_todo(id: int):
    try:
        return store_todo[id]
    except:
        return HTTPException(status_code=404, detail="Todo not found")


@app.put("/todo/{id}")
async def update_todo(id: int, todo: Todo):
    try:
        store_todo[id] = todo
        return store_todo[id]
    except:
        return HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todo/{id}")
async def delete_todo(id: int):
    try:
        object = store_todo[id]
        store_todo.pop(id)
        return object
    except:
        return HTTPException(status_code=404, detail="Todo not found")
