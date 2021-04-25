from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from config.database import SessionLocal

app = FastAPI()


# Dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"Hello": "World"}
