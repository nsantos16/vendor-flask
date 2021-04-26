from invoke import task

from src.vending_machine.models import VendingMachine
from src.item.models import Item
from config.database import get_db, Base


@task
def run(ctx):
    ctx.run("uvicorn main:app --reload")


@task
def init_db(ctx):
    print("Creating all resources.")
    Base.metadata.create_all()


@task
def drop_all(ctx):
    if input("Are you sure you want to drop all tables? (y/N)\n").lower() == "y":
        print("Dropping tables...")
        drop_all_db(Base)


@task
def seed_db(ctx):
    if (
            input(
                "Are you sure you want to drop all tables and recreate? (y/N)\n").lower()
            == "y"
    ):
        print("Dropping tables...")
        Base.metadata.drop_all()
        Base.metadata.create_all()
        seed_vending_machine(get_db)
        print("DB successfully seeded.")


def drop_all_db(base_class):
    base_class.metadata.drop_all()


def seed_vending_machine(getting_db_func):
    session = next(getting_db_func())
    vending_machine = VendingMachine()
    session.add(vending_machine)
    session.commit()
    items = [Item(name="Coca-cola", vending_machine=vending_machine),
             Item(name="Fanta", vending_machine=vending_machine),
             Item(name="Sprite", vending_machine=vending_machine)]
    session.add_all(items)
    session.commit()

