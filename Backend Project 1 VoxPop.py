from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# комментарий сақтауға арналған массив
comments = []

# комментарий моделі
class Comment(BaseModel):
    name: str
    content: str

@app.post("/comments/")
def add_comment(comment: Comment):
    # комментарийді массивке қосамыз
    comments.append({"name": comment.name, "content": comment.content})
    return {"message": "Комментарий қосылды", "comment": comment}

@app.get("/comments/", response_model=List[Comment])
def get_comments():
    # комментарии қайтарамыз
    return comments

