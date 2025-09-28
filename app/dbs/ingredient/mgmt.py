from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.ingredient.model import Ingredient
from typing import List


class IngredientMgmt:
    """Database management operations for ingredients."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[Ingredient]:
        """
        Retrieve all active ingredients from the database.
        
        Returns:
            List of Ingredient objects
        """
        query = select(Ingredient).where(Ingredient.is_active == True)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, ingredient_id: int) -> Ingredient | None:
        """
        Retrieve an ingredient by ID.
        
        Args:
            ingredient_id: The ingredient ID
            
        Returns:
            Ingredient object or None if not found
        """
        query = select(Ingredient).where(
            Ingredient.id == ingredient_id,
            Ingredient.is_active == True
        )
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, ingredient_data: dict) -> Ingredient:
        """
        Create a new ingredient.
        
        Args:
            ingredient_data: Dictionary containing ingredient data
            
        Returns:
            Created Ingredient object
        """
        ingredient = Ingredient(**ingredient_data)
        self.db.add(ingredient)
        await self.db.commit()
        await self.db.refresh(ingredient)
        return ingredient
    
    async def update(self, ingredient_id: int, update_data: dict) -> Ingredient | None:
        """
        Update an ingredient.
        
        Args:
            ingredient_id: The ingredient ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated Ingredient object or None if not found
        """
        ingredient = await self.get_by_id(ingredient_id)
        if not ingredient:
            return None
        
        for key, value in update_data.items():
            setattr(ingredient, key, value)
        
        await self.db.commit()
        await self.db.refresh(ingredient)
        return ingredient
    
    async def soft_delete(self, ingredient_id: int) -> bool:
        """
        Soft delete an ingredient by setting is_active to False.
        
        Args:
            ingredient_id: The ingredient ID
            
        Returns:
            True if deleted, False if not found
        """
        ingredient = await self.get_by_id(ingredient_id)
        if not ingredient:
            return False
        
        ingredient.is_active = False
        await self.db.commit()
        return True