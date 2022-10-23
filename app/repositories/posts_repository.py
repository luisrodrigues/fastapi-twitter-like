from sqlalchemy.orm import Session

from app.models import post_model
from app.schemas import post_schema


def read_all_posts(db: Session, limit):
    # fetch all posts
    return db.query(post_model.Post).limit(limit).all()


def create_post(request: post_schema.Post, db: Session, user_id: int):
    # create a post
    new_post = post_model.Post(title=request.title, body=request.body, user_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def read_post(post_id: int, db: Session):
    # fetch a post by id
    return db.query(post_model.Post).where(post_model.Post.id == post_id).first()


def delete_post(post_id: int, db: Session):
    # delete a post by id
    db.query(post_model.Post).filter(post_model.Post.id == post_id).delete(synchronize_session=False)
    db.commit()
    return {}


def update_post(post_id: int, request: post_schema.Post, db: Session):
    # update a post by id
    db.query(post_model.Post).filter(post_model.Post.id == post_id).update(request.dict())
    db.commit()
    return read_post(post_id, db)
