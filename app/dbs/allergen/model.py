from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Allergen(BaseModel):
    __tablename__ = "allergens"
    
    i18n_key = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    icon_url = Column(String(512))
    severity_level = Column(Integer, default=1)
    
    # Relationships
    menu_item_allergens = relationship("MenuItemAllergen", back_populates="allergen")