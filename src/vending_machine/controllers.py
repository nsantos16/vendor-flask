from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from config.database import get_db, engine
from src.constants import X_COINS

from .manager import get_coins_back, add_coins
from .schemas import PutCoinSchema
from . import models

models.Base.metadata.create_all(bind=engine)
router = APIRouter(
    tags=["Vending Machine"],
)


@router.put("/")
async def insert_coin(put_coin: PutCoinSchema, db: Session = Depends(get_db)):
    accepted_coins = add_coins(put_coin.coin, db)
    headers = {X_COINS: str(accepted_coins)}
    return Response(status_code=status.HTTP_204_NO_CONTENT, headers=headers)


@router.delete("/")
async def get_all_coins_back(db: Session = Depends(get_db)):
    coins_back = get_coins_back(db)
    headers = {X_COINS: str(coins_back)}
    return Response(status_code=status.HTTP_204_NO_CONTENT, headers=headers)
