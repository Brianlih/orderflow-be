from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from decimal import Decimal


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


class MenuItemResponse(BaseModel):
    """Schema for menu item response."""
    id: int
    name: str
    description: Optional[str]
    price: Decimal
    image_url: Optional[str]
    spice_level: int
    is_available: bool
    sort_order: int
    
    class Config:
        from_attributes = True


class CategoryWithMenuItemsResponse(BaseModel):
    """Schema for category with its menu items."""
    id: int
    name: str
    sort_order: int
    is_active: bool
    menu_items: List[MenuItemResponse] = []
    
    class Config:
        from_attributes = True


class RestaurantMenuResponse(BaseModel):
    """Schema for restaurant menu response organized by categories."""
    restaurant_id: int
    restaurant_name: str
    categories: List[CategoryWithMenuItemsResponse] = []