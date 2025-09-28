from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.menu_item.model import MenuItem
from typing import List


class MenuItemMgmt:
    """Database management operations for menu items."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[MenuItem]:
        """
        Retrieve all available menu items from the database.
        
        Returns:
            List of MenuItem objects
        """
        query = select(MenuItem).where(MenuItem.is_available == True)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, menu_item_id: int) -> MenuItem | None:
        """
        Retrieve a menu item by ID.
        
        Args:
            menu_item_id: The menu item ID
            
        Returns:
            MenuItem object or None if not found
        """
        query = select(MenuItem).where(
            MenuItem.id == menu_item_id,
            MenuItem.is_available == True
        )
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, menu_item_data: dict) -> MenuItem:
        """
        Create a new menu item.
        
        Args:
            menu_item_data: Dictionary containing menu item data
            
        Returns:
            Created MenuItem object
        """
        menu_item = MenuItem(**menu_item_data)
        self.db.add(menu_item)
        await self.db.commit()
        await self.db.refresh(menu_item)
        return menu_item
    
    async def update(self, menu_item_id: int, update_data: dict) -> MenuItem | None:
        """
        Update a menu item.
        
        Args:
            menu_item_id: The menu item ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated MenuItem object or None if not found
        """
        menu_item = await self.get_by_id(menu_item_id)
        if not menu_item:
            return None
        
        for key, value in update_data.items():
            setattr(menu_item, key, value)
        
        await self.db.commit()
        await self.db.refresh(menu_item)
        return menu_item
    
    async def soft_delete(self, menu_item_id: int) -> bool:
        """
        Soft delete a menu item by setting is_available to False.
        
        Args:
            menu_item_id: The menu item ID
            
        Returns:
            True if deleted, False if not found
        """
        menu_item = await self.get_by_id(menu_item_id)
        if not menu_item:
            return False
        
        menu_item.is_available = False
        await self.db.commit()
        return True