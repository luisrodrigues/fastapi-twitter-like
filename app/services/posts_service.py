from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.repositories import posts_repository
from app.repositories import users_repository
from app.schemas.post_schema import Post
from app.schemas.user_schema import User


def check_post_exists(post_id: int, post: Post):
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} was not found")


def read_all_posts(db: Session, limit):
    # fetch all posts
    return posts_repository.read_all_posts(db, limit)


def create_post(request: Post, db: Session, current_user: User):
    # create a post
    user = users_repository.get_user_by_email(current_user.email, db)
    return posts_repository.create_post(request, db, user.id)


def read_post(post_id: int, db: Session):
    # fetch a post by id
    post = posts_repository.read_post(post_id, db)
    check_post_exists(post_id, post)
    return post


def delete_post(post_id: int, db: Session):
    # delete a post by id
    post = read_post(post_id, db)
    check_post_exists(post_id, post)
    return posts_repository.delete_post(post_id, db)


def update_post(post_id: int, request: Post, db: Session):
    # update a post by id
    post = read_post(post_id, db)
    check_post_exists(post_id, post)
    return posts_repository.update_post(post_id, request, db)
