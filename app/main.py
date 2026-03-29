from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.core.database import Base, engine
from app.core.deps import get_db

import app.models.user
import app.models.content
import app.models.skill
import app.models.interaction

from app.repository.user_repository import UserRepository

app = FastAPI(title="Recommendation System API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return repo.create_user(name, email)


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return repo.get_all_users()