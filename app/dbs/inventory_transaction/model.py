from sqlalchemy import Column, String, Integer, ForeignKey, DECIMAL, Enum
from sqlalchemy.orm import relationship
from app.models.base import BaseModel
import enum


class TransactionType(enum.Enum):
    waste = "waste"
    order_consumption = "order_consumption"
    adjustment = "adjustment"
    restock = "restock"


class InventoryTransaction(BaseModel):
    __tablename__ = "inventory_transactions"
    
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    order_item_id = Column(Integer, ForeignKey("order_items.order_item_id"), nullable=True)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    quantity_change = Column(DECIMAL(10, 3), nullable=False)
    quantity_before = Column(DECIMAL(10, 3), nullable=False)
    quantity_after = Column(DECIMAL(10, 3), nullable=False)
    notes = Column(String(255))
    staff_id = Column(Integer, nullable=True)  # FK to staff table (not defined in ERD)
    
    # Relationships
    ingredient = relationship("Ingredient", back_populates="inventory_transactions")
    order = relationship("Order", back_populates="inventory_transactions")
    order_item = relationship("OrderItem", back_populates="inventory_transactions")