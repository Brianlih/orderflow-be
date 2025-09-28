from sqlalchemy import Column, String, Text, Integer, Boolean, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class MenuItem(BaseModel):
    __tablename__ = "menu_items"
    
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    image_url = Column(String(512))
    spice_level = Column(Integer, default=0)  # Using Integer instead of TINYINT for SQLAlchemy compatibility
    is_available = Column(Boolean, default=True)
    sort_order = Column(Integer, default=0)
    deleted_at = Column(DateTime(timezone=True))
    
    # Relationships
    restaurant = relationship("Restaurant", back_populates="menu_items")
    category = relationship("Category", back_populates="menu_items")
    order_items = relationship("OrderItem", back_populates="menu_item")
    customization_options = relationship("CustomizationOption", back_populates="menu_item")
    menu_item_allergens = relationship("MenuItemAllergen", back_populates="menu_item")
    menu_item_recipes = relationship("MenuItemRecipe", back_populates="menu_item")