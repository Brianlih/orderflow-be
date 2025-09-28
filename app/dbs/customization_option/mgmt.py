from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.customization_option.model import CustomizationOption
from typing import List


class CustomizationOptionMgmt:
    """Database management operations for customization options."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[CustomizationOption]:
        """
        Retrieve all active customization options from the database.
        
        Returns:
            List of CustomizationOption objects
        """
        query = select(CustomizationOption).where(CustomizationOption.is_active == True)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, option_id: int) -> CustomizationOption | None:
        """
        Retrieve a customization option by ID.
        
        Args:
            option_id: The customization option ID
            
        Returns:
            CustomizationOption object or None if not found
        """
        query = select(CustomizationOption).where(
            CustomizationOption.id == option_id,
            CustomizationOption.is_active == True
        )
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, option_data: dict) -> CustomizationOption:
        """
        Create a new customization option.
        
        Args:
            option_data: Dictionary containing customization option data
            
        Returns:
            Created CustomizationOption object
        """
        option = CustomizationOption(**option_data)
        self.db.add(option)
        await self.db.commit()
        await self.db.refresh(option)
        return option
    
    async def update(self, option_id: int, update_data: dict) -> CustomizationOption | None:
        """
        Update a customization option.
        
        Args:
            option_id: The customization option ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated CustomizationOption object or None if not found
        """
        option = await self.get_by_id(option_id)
        if not option:
            return None
        
        for key, value in update_data.items():
            setattr(option, key, value)
        
        await self.db.commit()
        await self.db.refresh(option)
        return option
    
    async def soft_delete(self, option_id: int) -> bool:
        """
        Soft delete a customization option by setting is_active to False.
        
        Args:
            option_id: The customization option ID
            
        Returns:
            True if deleted, False if not found
        """
        option = await self.get_by_id(option_id)
        if not option:
            return False
        
        option.is_active = False
        await self.db.commit()
        return True