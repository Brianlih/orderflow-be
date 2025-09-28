from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.restaurant.model import Restaurant
from typing import List


class RestaurantMgmt:
    """Database management operations for restaurants."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[Restaurant]:
        """
        Retrieve all active restaurants from the database.
        
        Returns:
            List of Restaurant objects
        """
        query = select(Restaurant).where(Restaurant.is_active == True)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, restaurant_id: int) -> Restaurant | None:
        """
        Retrieve a restaurant by ID.
        
        Args:
            restaurant_id: The restaurant ID
            
        Returns:
            Restaurant object or None if not found
        """
        query = select(Restaurant).where(
            Restaurant.id == restaurant_id,
            Restaurant.is_active == True
        )
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, restaurant_data: dict) -> Restaurant:
        """
        Create a new restaurant.
        
        Args:
            restaurant_data: Dictionary containing restaurant data
            
        Returns:
            Created Restaurant object
        """
        restaurant = Restaurant(**restaurant_data)
        self.db.add(restaurant)
        await self.db.commit()
        await self.db.refresh(restaurant)
        return restaurant
    
    async def update(self, restaurant_id: int, update_data: dict) -> Restaurant | None:
        """
        Update a restaurant.
        
        Args:
            restaurant_id: The restaurant ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated Restaurant object or None if not found
        """
        restaurant = await self.get_by_id(restaurant_id)
        if not restaurant:
            return None
        
        for key, value in update_data.items():
            setattr(restaurant, key, value)
        
        await self.db.commit()
        await self.db.refresh(restaurant)
        return restaurant
    
    async def soft_delete(self, restaurant_id: int) -> bool:
        """
        Soft delete a restaurant by setting is_active to False.
        
        Args:
            restaurant_id: The restaurant ID
            
        Returns:
            True if deleted, False if not found
        """
        restaurant = await self.get_by_id(restaurant_id)
        if not restaurant:
            return False
        
        restaurant.is_active = False
        await self.db.commit()
        return True