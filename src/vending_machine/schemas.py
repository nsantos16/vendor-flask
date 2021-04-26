from fastapi import HTTPException, status
from typing import List, Optional
from pydantic import BaseModel, validator

from src.item.schemas import Item
from config.settings import settings


class VendingMachineBase(BaseModel):
    saved_coins: int


class PutCoinSchema(BaseModel):
    coin: int

    @validator("coin")
    def coins_accepted(cls, coin):
        if coin <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="The number of coins must be positive")

        if not settings.feat_flag_more_than_one_coin and coin > 1:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="No more than one coin is allowed at a time")

        return coin


class VendingMachine(VendingMachineBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True
