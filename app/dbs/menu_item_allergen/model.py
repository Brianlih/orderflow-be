from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum


class ContaminationRisk(enum.Enum):
    contains = "contains"
    may_contain = "may_contain"


class MenuItemAllergen(Base):
    __tablename__ = "menu_item_allergens"
    
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), primary_key=True)
    allergen_id = Column(Integer, ForeignKey("allergens.id"), primary_key=True)
    contamination_risk = Column(Enum(ContaminationRisk), nullable=False)
    
    # Relationships
    menu_item = relationship("MenuItem", back_populates="menu_item_allergens")
    allergen = relationship("Allergen", back_populates="menu_item_allergens")