from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class MenuItemRecipe(BaseModel):
    __tablename__ = "menu_item_recipes"
    
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), nullable=False)
    quantity_needed = Column(DECIMAL(10, 3), nullable=False)
    unit = Column(String(20))
    is_critical = Column(Boolean, default=False)
    notes = Column(String(255))
    
    # Relationships
    menu_item = relationship("MenuItem", back_populates="menu_item_recipes")
    ingredient = relationship("Ingredient", back_populates="menu_item_recipes")