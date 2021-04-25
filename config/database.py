from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from .settings import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_user}" \
                          f":{settings.database_password}" \
                          f"@{settings.database_host}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.bind = engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
