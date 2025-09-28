from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.menu_item_allergen.model import MenuItemAllergen
from typing import List


class MenuItemAllergenMgmt:
    """Database management operations for menu item allergens."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[MenuItemAllergen]:
        """
        Retrieve all menu item allergens from the database.
        
        Returns:
            List of MenuItemAllergen objects
        """
        query = select(MenuItemAllergen)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_ids(self, menu_item_id: int, allergen_id: int) -> MenuItemAllergen | None:
        """
        Retrieve a menu item allergen by menu item ID and allergen ID.
        
        Args:
            menu_item_id: The menu item ID
            allergen_id: The allergen ID
            
        Returns:
            MenuItemAllergen object or None if not found
        """
        query = select(MenuItemAllergen).where(
            MenuItemAllergen.menu_item_id == menu_item_id,
            MenuItemAllergen.allergen_id == allergen_id
        )
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, allergen_data: dict) -> MenuItemAllergen:
        """
        Create a new menu item allergen.
        
        Args:
            allergen_data: Dictionary containing menu item allergen data
            
        Returns:
            Created MenuItemAllergen object
        """
        allergen = MenuItemAllergen(**allergen_data)
        self.db.add(allergen)
        await self.db.commit()
        await self.db.refresh(allergen)
        return allergen
    
    async def update(self, menu_item_id: int, allergen_id: int, update_data: dict) -> MenuItemAllergen | None:
        """
        Update a menu item allergen.
        
        Args:
            menu_item_id: The menu item ID
            allergen_id: The allergen ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated MenuItemAllergen object or None if not found
        """
        allergen = await self.get_by_ids(menu_item_id, allergen_id)
        if not allergen:
            return None
        
        for key, value in update_data.items():
            setattr(allergen, key, value)
        
        await self.db.commit()
        await self.db.refresh(allergen)
        return allergen