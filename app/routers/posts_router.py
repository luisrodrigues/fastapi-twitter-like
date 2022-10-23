from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.post_schema import Post, ShowPost
from app.schemas.user_schema import User
from app.security import oauth2
from app.services import posts_service

router = APIRouter()


@router.get("/", response_model=List[ShowPost])
def read_all_posts(db: Session = Depends(get_db), limit: int = 10,
                   current_user: User = Depends(oauth2.get_current_user)):
    # fetch all posts
    return posts_service.read_all_posts(db, limit)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ShowPost)
def create_post(request: Post, db: Session = Depends(get_db),
                current_user: User = Depends(oauth2.get_current_user)):
    # create a post
    return posts_service.create_post(request, db, current_user)


@router.get("/{post_id}", status_code=status.HTTP_200_OK, response_model=ShowPost)
def read_post(post_id: int, db: Session = Depends(get_db),
              current_user: User = Depends(oauth2.get_current_user)):
    # fetch a post by id
    return posts_service.read_post(post_id, db)


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db),
                current_user: User = Depends(oauth2.get_current_user)):
    # delete a post by id
    return posts_service.delete_post(post_id, db)


@router.put("/{post_id}", status_code=status.HTTP_202_ACCEPTED, response_model=ShowPost)
def update_post(post_id: int, request: Post, db: Session = Depends(get_db),
                current_user: User = Depends(oauth2.get_current_user)):
    # update a post by id
    return posts_service.update_post(post_id, request, db)
