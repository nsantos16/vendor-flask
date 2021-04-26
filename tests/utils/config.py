from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.database import Base, get_db
from config.settings import settings
from main import app

SQLALCHEMY_TEST_DATABASE_URL = f"postgresql://{settings.test_database_user}" \
                          f":{settings.test_database_password}" \
                          f"@{settings.test_database_host}/{settings.test_database_name}"

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)
