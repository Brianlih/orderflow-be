from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class CustomizationChoice(BaseModel):
    __tablename__ = "customization_choices"
    
    option_id = Column(Integer, ForeignKey("customization_options.id"), nullable=False)
    name = Column(String(50), nullable=False)
    price_modifier = Column(DECIMAL(10, 2), default=0)
    is_available = Column(Boolean, default=True)
    sort_order = Column(Integer, default=0)
    
    # Relationships
    customization_option = relationship("CustomizationOption", back_populates="customization_choices")
    order_customizations = relationship("OrderCustomization", back_populates="customization_choice")