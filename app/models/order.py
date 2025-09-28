from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Order(BaseModel):
    __tablename__ = "orders"
    
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    table_id = Column(Integer, ForeignKey("tables.id"), nullable=False)
    subtotal = Column(DECIMAL(10, 2), nullable=False)
    service_charge = Column(DECIMAL(10, 2), default=0)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    status = Column(String(50), default="pending")
    payment_status = Column(String(50), default="pending")
    payment_method = Column(String(50))
    special_requests = Column(Text)
    order_time = Column(DateTime(timezone=True))
    estimated_ready_time = Column(DateTime(timezone=True))
    completed_time = Column(DateTime(timezone=True))
    deleted_at = Column(DateTime(timezone=True))
    
    # Relationships
    restaurant = relationship("Restaurant", back_populates="orders")
    table = relationship("Table", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")
    inventory_transactions = relationship("InventoryTransaction", back_populates="order")