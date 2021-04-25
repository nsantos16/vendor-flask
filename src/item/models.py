from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    stock = Column(Integer, default=5)
    vending_machine_id = Column(Integer, ForeignKey("vending_machines.id"))

    vending_machine = relationship("VendingMachine", back_populates="items")
