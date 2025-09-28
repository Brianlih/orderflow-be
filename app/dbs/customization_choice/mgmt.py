from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.customization_choice.model import CustomizationChoice
from typing import List


class CustomizationChoiceMgmt:
    """Database management operations for customization choices."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[CustomizationChoice]:
        """
        Retrieve all customization choices from the database.
        
        Returns:
            List of CustomizationChoice objects
        """
        query = select(CustomizationChoice)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, choice_id: int) -> CustomizationChoice | None:
        """
        Retrieve a customization choice by ID.
        
        Args:
            choice_id: The customization choice ID
            
        Returns:
            CustomizationChoice object or None if not found
        """
        query = select(CustomizationChoice).where(CustomizationChoice.id == choice_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, choice_data: dict) -> CustomizationChoice:
        """
        Create a new customization choice.
        
        Args:
            choice_data: Dictionary containing customization choice data
            
        Returns:
            Created CustomizationChoice object
        """
        choice = CustomizationChoice(**choice_data)
        self.db.add(choice)
        await self.db.commit()
        await self.db.refresh(choice)
        return choice
    
    async def update(self, choice_id: int, update_data: dict) -> CustomizationChoice | None:
        """
        Update a customization choice.
        
        Args:
            choice_id: The customization choice ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated CustomizationChoice object or None if not found
        """
        choice = await self.get_by_id(choice_id)
        if not choice:
            return None
        
        for key, value in update_data.items():
            setattr(choice, key, value)
        
        await self.db.commit()
        await self.db.refresh(choice)
        return choice