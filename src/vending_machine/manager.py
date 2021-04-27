from sqlalchemy.orm import Session

from .helpers import get_vending_machine


def get_saved_coins(db: Session):
    vending_machine = get_vending_machine(db)
    return vending_machine.saved_coins


def get_coins_back(db: Session):
    vending_machine = get_vending_machine(db)
    saved_coins = vending_machine.saved_coins
    vending_machine.saved_coins = 0
    db.commit()
    return saved_coins


def add_coins(coins: int, db: Session):
    vending_machine = get_vending_machine(db)
    vending_machine.saved_coins += coins
    db.commit()
    return vending_machine.saved_coins
