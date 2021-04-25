from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_db

router = APIRouter(
    tags=["Vending Machine"],
)


@router.put("/")
async def insert_coin(db: Session = Depends(get_db)):
    pass


@router.delete("/")
async def get_all_coins_back(db: Session = Depends(get_db)):
    pass
