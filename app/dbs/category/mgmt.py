from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.category.model import Category
from typing import List


class CategoryMgmt:
    """Database management operations for categories."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[Category]:
        """
        Retrieve all active categories from the database.
        
        Returns:
            List of Category objects
        """
        query = select(Category).where(Category.is_active == True)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, category_id: int) -> Category | None:
        """
        Retrieve a category by ID.
        
        Args:
            category_id: The category ID
            
        Returns:
            Category object or None if not found
        """
        query = select(Category).where(
            Category.id == category_id,
            Category.is_active == True
        )
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, category_data: dict) -> Category:
        """
        Create a new category.
        
        Args:
            category_data: Dictionary containing category data
            
        Returns:
            Created Category object
        """
        category = Category(**category_data)
        self.db.add(category)
        await self.db.commit()
        await self.db.refresh(category)
        return category
    
    async def update(self, category_id: int, update_data: dict) -> Category | None:
        """
        Update a category.
        
        Args:
            category_id: The category ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated Category object or None if not found
        """
        category = await self.get_by_id(category_id)
        if not category:
            return None
        
        for key, value in update_data.items():
            setattr(category, key, value)
        
        await self.db.commit()
        await self.db.refresh(category)
        return category
    
    async def soft_delete(self, category_id: int) -> bool:
        """
        Soft delete a category by setting is_active to False.
        
        Args:
            category_id: The category ID
            
        Returns:
            True if deleted, False if not found
        """
        category = await self.get_by_id(category_id)
        if not category:
            return False
        
        category.is_active = False
        await self.db.commit()
        return True