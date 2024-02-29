from fastapi import APIRouter, Depends
from app.auth.jwt_bearer import jwtBearer
from app.models.post import PostSchema


router = APIRouter()

posts = [
    {
        "id": 1,
        "title": "Hello World",
        "content": "This is a blog post"
    },
    {
        "id": 2,
        "title": "Hello World",
        "content": "This is a blog post"
    }
]

@router.get("/", tags=["posts"], dependencies=[Depends(jwtBearer())])
async def read_all():
    return {"data": posts}

@router.get("/{post_id}", tags=["posts"], dependencies=[Depends(jwtBearer())])
async def read_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return {"data": post}
    return {"Error": "Post not found"}

@router.post("/", tags=["posts"], dependencies=[Depends(jwtBearer())])
async def create_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.model_dump()) 
    return {"data": "Post created"}