from fastapi import APIRouter, Depends, status, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config.database import get_db, engine
from src.constants import INVENTORY_ENDPOINT, X_COINS, X_INVENTORY_REMAINING

from . import models
from .manager import get_items, buy_item as buy_item_manager

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix=INVENTORY_ENDPOINT,
    tags=["Inventory"],
)


@router.get("/")
async def get_remaining_items(db: Session = Depends(get_db)):
    items = get_items(db)
    return items


@router.put("/{item_id}")
async def buy_item(item_id: int, db: Session = Depends(get_db)):
    x_coins, response_status, item_qty = buy_item_manager(item_id, db)
    headers = {X_COINS: str(x_coins)}

    if response_status == status.HTTP_200_OK:
        headers[X_INVENTORY_REMAINING] = str(item_qty)
        return JSONResponse(content={"quantity": item_qty}, status_code=response_status, headers=headers)

    return Response(status_code=response_status, headers=headers)
