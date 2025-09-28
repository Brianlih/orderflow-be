from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.allergen.model import Allergen
from typing import List


class AllergenMgmt:
    """Database management operations for allergens."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[Allergen]:
        """
        Retrieve all allergens from the database.
        
        Returns:
            List of Allergen objects
        """
        query = select(Allergen)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, allergen_id: int) -> Allergen | None:
        """
        Retrieve an allergen by ID.
        
        Args:
            allergen_id: The allergen ID
            
        Returns:
            Allergen object or None if not found
        """
        query = select(Allergen).where(Allergen.id == allergen_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, allergen_data: dict) -> Allergen:
        """
        Create a new allergen.
        
        Args:
            allergen_data: Dictionary containing allergen data
            
        Returns:
            Created Allergen object
        """
        allergen = Allergen(**allergen_data)
        self.db.add(allergen)
        await self.db.commit()
        await self.db.refresh(allergen)
        return allergen
    
    async def update(self, allergen_id: int, update_data: dict) -> Allergen | None:
        """
        Update an allergen.
        
        Args:
            allergen_id: The allergen ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated Allergen object or None if not found
        """
        allergen = await self.get_by_id(allergen_id)
        if not allergen:
            return None
        
        for key, value in update_data.items():
            setattr(allergen, key, value)
        
        await self.db.commit()
        await self.db.refresh(allergen)
        return allergen