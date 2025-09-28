from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.table.model import Table
from typing import List


class TableMgmt:
    """Database management operations for tables."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[Table]:
        """
        Retrieve all tables from the database.
        
        Returns:
            List of Table objects
        """
        query = select(Table)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, table_id: int) -> Table | None:
        """
        Retrieve a table by ID.
        
        Args:
            table_id: The table ID
            
        Returns:
            Table object or None if not found
        """
        query = select(Table).where(Table.id == table_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, table_data: dict) -> Table:
        """
        Create a new table.
        
        Args:
            table_data: Dictionary containing table data
            
        Returns:
            Created Table object
        """
        table = Table(**table_data)
        self.db.add(table)
        await self.db.commit()
        await self.db.refresh(table)
        return table
    
    async def update(self, table_id: int, update_data: dict) -> Table | None:
        """
        Update a table.
        
        Args:
            table_id: The table ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated Table object or None if not found
        """
        table = await self.get_by_id(table_id)
        if not table:
            return None
        
        for key, value in update_data.items():
            setattr(table, key, value)
        
        await self.db.commit()
        await self.db.refresh(table)
        return table