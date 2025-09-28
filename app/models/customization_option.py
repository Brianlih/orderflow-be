from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class CustomizationOption(BaseModel):
    __tablename__ = "customization_options"
    
    item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    name = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    is_required = Column(Boolean, default=False)
    max_selections = Column(Integer, default=1)
    sort_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    menu_item = relationship("MenuItem", back_populates="customization_options")
    customization_choices = relationship("CustomizationChoice", back_populates="customization_option")
    order_customizations = relationship("OrderCustomization", back_populates="customization_option")