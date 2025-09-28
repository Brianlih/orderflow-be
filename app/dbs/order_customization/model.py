from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class OrderCustomization(BaseModel):
    __tablename__ = "order_customizations"
    
    order_item_id = Column(Integer, ForeignKey("order_items.order_item_id"), nullable=False)
    option_id = Column(Integer, ForeignKey("customization_options.id"), nullable=False)
    choice_id = Column(Integer, ForeignKey("customization_choices.id"), nullable=False)
    price_modifier = Column(DECIMAL(10, 2), default=0)
    
    # Relationships
    order_item = relationship("OrderItem", back_populates="order_customizations")
    customization_option = relationship("CustomizationOption", back_populates="order_customizations")
    customization_choice = relationship("CustomizationChoice", back_populates="order_customizations")