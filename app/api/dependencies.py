from app.db.db import SessionLocal, init_db


def get_db():
    init_db()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
