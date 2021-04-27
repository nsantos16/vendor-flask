from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from src.vending_machine.helpers import get_vending_machine
from src.vending_machine.models import VendingMachine

from .models import Item

ITEM_PRICE = 2


def get_items(db: Session):
    vending_machine = get_vending_machine(db)
    [delattr(item, "vending_machine_id") for item in vending_machine.items]
    sorted_items = sorted(vending_machine.items, key=lambda k: k.id)
    return sorted_items


def _empty_saved_coins(vending_machine: VendingMachine, db: Session):
    coins_accepted = vending_machine.saved_coins
    vending_machine.saved_coins = 0
    db.commit()

    return coins_accepted


def buy_item(item_id: int, db: Session):
    vending_machine = get_vending_machine(db)
    item = db.query(Item).get(item_id)

    if item is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item id invalid")

    coins_accepted = _empty_saved_coins(vending_machine, db)

    if item.stock == 0:
        return coins_accepted, status.HTTP_404_NOT_FOUND, None

    if coins_accepted < 2:
        return coins_accepted, status.HTTP_400_BAD_REQUEST, None

    item.stock -= 1
    db.commit()

    return coins_accepted - ITEM_PRICE, status.HTTP_200_OK, item.stock



