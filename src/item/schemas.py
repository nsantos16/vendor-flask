from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    stock: int


class Item(ItemBase):
    id: int
    vending_machine_id: int

    class Config:
        orm_mode = True
