from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Table(BaseModel):
    __tablename__ = "tables"
    
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    name = Column(String(50), nullable=False)
    qr_code_token = Column(String(50), unique=True)
    status = Column(String(50), default="available")
    deleted_at = Column(DateTime(timezone=True))
    
    # Relationships
    restaurant = relationship("Restaurant", back_populates="tables")
    orders = relationship("Order", back_populates="table")
    qr_sessions = relationship("QRSession", back_populates="table")