from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.order_customization.model import OrderCustomization
from typing import List


class OrderCustomizationMgmt:
    """Database management operations for order customizations."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[OrderCustomization]:
        """
        Retrieve all order customizations from the database.
        
        Returns:
            List of OrderCustomization objects
        """
        query = select(OrderCustomization)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, customization_id: int) -> OrderCustomization | None:
        """
        Retrieve an order customization by ID.
        
        Args:
            customization_id: The order customization ID
            
        Returns:
            OrderCustomization object or None if not found
        """
        query = select(OrderCustomization).where(OrderCustomization.id == customization_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, customization_data: dict) -> OrderCustomization:
        """
        Create a new order customization.
        
        Args:
            customization_data: Dictionary containing order customization data
            
        Returns:
            Created OrderCustomization object
        """
        customization = OrderCustomization(**customization_data)
        self.db.add(customization)
        await self.db.commit()
        await self.db.refresh(customization)
        return customization
    
    async def update(self, customization_id: int, update_data: dict) -> OrderCustomization | None:
        """
        Update an order customization.
        
        Args:
            customization_id: The order customization ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated OrderCustomization object or None if not found
        """
        customization = await self.get_by_id(customization_id)
        if not customization:
            return None
        
        for key, value in update_data.items():
            setattr(customization, key, value)
        
        await self.db.commit()
        await self.db.refresh(customization)
        return customization