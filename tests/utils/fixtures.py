import pytest

from tasks import seed_vending_machine

from .config import override_get_db, Base, engine


@pytest.fixture(scope="module", autouse=True)
def init_db():
    seed_vending_machine(override_get_db)
    yield
    Base.metadata.drop_all(bind=engine)
