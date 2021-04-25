from typing import List, Optional
from pydantic import BaseModel

from src.item.schemas import Item


class VendingMachineBase(BaseModel):
    saved_coins: int


class VendingMachine(VendingMachineBase):
    id: int
    items: List[Item] = []
