from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.menu_item_recipe.model import MenuItemRecipe
from typing import List


class MenuItemRecipeMgmt:
    """Database management operations for menu item recipes."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[MenuItemRecipe]:
        """
        Retrieve all menu item recipes from the database.
        
        Returns:
            List of MenuItemRecipe objects
        """
        query = select(MenuItemRecipe)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, recipe_id: int) -> MenuItemRecipe | None:
        """
        Retrieve a menu item recipe by ID.
        
        Args:
            recipe_id: The menu item recipe ID
            
        Returns:
            MenuItemRecipe object or None if not found
        """
        query = select(MenuItemRecipe).where(MenuItemRecipe.id == recipe_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, recipe_data: dict) -> MenuItemRecipe:
        """
        Create a new menu item recipe.
        
        Args:
            recipe_data: Dictionary containing menu item recipe data
            
        Returns:
            Created MenuItemRecipe object
        """
        recipe = MenuItemRecipe(**recipe_data)
        self.db.add(recipe)
        await self.db.commit()
        await self.db.refresh(recipe)
        return recipe
    
    async def update(self, recipe_id: int, update_data: dict) -> MenuItemRecipe | None:
        """
        Update a menu item recipe.
        
        Args:
            recipe_id: The menu item recipe ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated MenuItemRecipe object or None if not found
        """
        recipe = await self.get_by_id(recipe_id)
        if not recipe:
            return None
        
        for key, value in update_data.items():
            setattr(recipe, key, value)
        
        await self.db.commit()
        await self.db.refresh(recipe)
        return recipe