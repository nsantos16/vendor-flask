from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_db

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"],
)


@router.get("/")
async def get_remaining_items(db: Session = Depends(get_db)):
    pass


@router.put("/{item_id}")
async def buy_item(item_id: int, db: Session = Depends(get_db)):
    pass
