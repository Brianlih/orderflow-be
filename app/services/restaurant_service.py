from sqlalchemy.ext.asyncio import AsyncSession
from app.dbs.restaurant.model import Restaurant
from app.dbs.restaurant.mgmt import RestaurantMgmt
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