from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from config.database import Base


class VendingMachine(Base):
    __tablename__ = "vending_machines"

    id = Column(Integer, primary_key=True, index=True)
    saved_coins = Column(Integer, default=0)

    items = relationship("Item", back_populates="vending_machine")
