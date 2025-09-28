from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Ingredient(BaseModel):
    __tablename__ = "ingredients"
    
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    name = Column(String(50), nullable=False)
    sku_code = Column(String(50))
    unit = Column(String(20))
    unit_cost = Column(DECIMAL(10, 2))
    min_threshold = Column(Integer, default=0)
    max_capacity = Column(Integer)
    category = Column(String(50))
    storage_location = Column(String(100))
    shelf_life_days = Column(Integer)
    is_active = Column(Boolean, default=True)
    deleted_at = Column(DateTime(timezone=True))
    
    # Relationships
    restaurant = relationship("Restaurant", back_populates="ingredients")
    menu_item_recipes = relationship("MenuItemRecipe", back_populates="ingredient")
    inventory_transactions = relationship("InventoryTransaction", back_populates="ingredient")