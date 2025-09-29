from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, distinct
from app.dbs.restaurant.model import Restaurant
from app.dbs.restaurant.mgmt import RestaurantMgmt
from app.dbs.allergen.model import Allergen
from app.dbs.menu_item.model import MenuItem
from app.dbs.menu_item_allergen.model import MenuItemAllergen
from app.dbs.category.model import Category
from typing import List


class RestaurantService:
    """Service for restaurant business logic."""
    
    def __init__(self, db: AsyncSession):
        self.mgmt = RestaurantMgmt(db)
    
    async def get_all_restaurants(self) -> List[Restaurant]:
        """
        Get all active restaurants.
        
        Returns:
            List of Restaurant objects
        """
        return await self.mgmt.get_all_active()
    
    async def get_restaurant_by_id(self, restaurant_id: int) -> Restaurant | None:
        """
        Get a restaurant by ID.
        
        Args:
            restaurant_id: The restaurant ID
            
        Returns:
            Restaurant object or None if not found
        """
        return await self.mgmt.get_by_id(restaurant_id)
    
    async def create_restaurant(self, restaurant_data: dict) -> Restaurant:
        """
        Create a new restaurant.
        
        Args:
            restaurant_data: Dictionary containing restaurant data
            
        Returns:
            Created Restaurant object
        """
        return await self.mgmt.create(restaurant_data)
    
    async def update_restaurant(self, restaurant_id: int, update_data: dict) -> Restaurant | None:
        """
        Update a restaurant.
        
        Args:
            restaurant_id: The restaurant ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated Restaurant object or None if not found
        """
        return await self.mgmt.update(restaurant_id, update_data)
    
    async def delete_restaurant(self, restaurant_id: int) -> bool:
        """
        Soft delete a restaurant.
        
        Args:
            restaurant_id: The restaurant ID
            
        Returns:
            True if deleted, False if not found
        """
        return await self.mgmt.soft_delete(restaurant_id)
    
    async def get_restaurant_allergens(self, restaurant_id: int) -> List[Allergen]:
        """
        Get all unique allergens associated with a restaurant's menu items.
        
        Args:
            restaurant_id: The restaurant ID
            
        Returns:
            List of unique Allergen objects for the restaurant
        """
        # Query to get distinct allergens for a restaurant through menu items
        stmt = (
            select(distinct(Allergen.id), Allergen)
            .join(MenuItemAllergen, Allergen.id == MenuItemAllergen.allergen_id)
            .join(MenuItem, MenuItemAllergen.menu_item_id == MenuItem.id)
            .where(MenuItem.restaurant_id == restaurant_id)
            .order_by(Allergen.name)
        )
        
        result = await self.mgmt.db.execute(stmt)
        allergens = result.scalars().unique().all()
        return list(allergens)
    
    async def get_restaurant_menu(self, restaurant_id: int) -> dict:
        """
        Get restaurant menu organized by categories with menu items.
        
        Args:
            restaurant_id: The restaurant ID
            
        Returns:
            Dictionary containing restaurant info and categorized menu items
        """
        # Get restaurant info
        restaurant = await self.get_restaurant_by_id(restaurant_id)
        
        # Get categories with their menu items
        stmt = (
            select(Category)
            .where(Category.restaurant_id == restaurant_id)
            .where(Category.is_active == True)
            .order_by(Category.sort_order, Category.name)
        )
        
        result = await self.mgmt.db.execute(stmt)
        categories = result.scalars().all()
        
        # For each category, get its menu items
        categories_data = []
        for category in categories:
            menu_items_stmt = (
                select(MenuItem)
                .where(MenuItem.category_id == category.id)
                .where(MenuItem.is_available == True)
                .order_by(MenuItem.sort_order, MenuItem.name)
            )
            
            menu_items_result = await self.mgmt.db.execute(menu_items_stmt)
            menu_items = menu_items_result.scalars().all()
            
            category_data = {
                "id": category.id,
                "name": category.name,
                "sort_order": category.sort_order,
                "is_active": category.is_active,
                "created_at": category.created_at,
                "updated_at": category.updated_at,
                "menu_items": list(menu_items)
            }
            categories_data.append(category_data)
        
        return {
            "restaurant_id": restaurant_id,
            "restaurant_name": restaurant.name,
            "categories": categories_data
        }