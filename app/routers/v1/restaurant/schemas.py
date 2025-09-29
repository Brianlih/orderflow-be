from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class RestaurantBase(BaseModel):
    """Base restaurant schema with common fields."""
    name: str = Field(..., max_length=50, description="Restaurant name")
    address: Optional[str] = Field(None, max_length=50, description="Restaurant address")
    phone: Optional[str] = Field(None, max_length=50, description="Restaurant phone number")
    email: Optional[str] = Field(None, max_length=50, description="Restaurant email")
    description: Optional[str] = Field(None, description="Restaurant description")


class RestaurantCreate(RestaurantBase):
    """Schema for creating a new restaurant."""
    pass


class RestaurantUpdate(BaseModel):
    """Schema for updating a restaurant."""
    name: Optional[str] = Field(None, max_length=50, description="Restaurant name")
    address: Optional[str] = Field(None, max_length=50, description="Restaurant address")
    phone: Optional[str] = Field(None, max_length=50, description="Restaurant phone number")
    email: Optional[str] = Field(None, max_length=50, description="Restaurant email")
    description: Optional[str] = Field(None, description="Restaurant description")


class RestaurantResponse(RestaurantBase):
    """Schema for restaurant response."""
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True


class AllergenResponse(BaseModel):
    """Schema for allergen response."""
    id: int
    i18n_key: str
    name: str
    icon_url: Optional[str]
    
    class Config:
        from_attributes = True