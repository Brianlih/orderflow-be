from sqlalchemy import Column, String, Text, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Restaurant(BaseModel):
    __tablename__ = "restaurants"
    
    name = Column(String(50), nullable=False)
    address = Column(String(50))
    phone = Column(String(50))
    email = Column(String(50))
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    deleted_at = Column(DateTime(timezone=True))
    
    # Relationships
    tables = relationship("Table", back_populates="restaurant")
    categories = relationship("Category", back_populates="restaurant")
    menu_items = relationship("MenuItem", back_populates="restaurant")
    ingredients = relationship("Ingredient", back_populates="restaurant")
    orders = relationship("Order", back_populates="restaurant")