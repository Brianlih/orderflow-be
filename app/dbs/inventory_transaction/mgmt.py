from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.inventory_transaction.model import InventoryTransaction
from typing import List


class InventoryTransactionMgmt:
    """Database management operations for inventory transactions."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[InventoryTransaction]:
        """
        Retrieve all inventory transactions from the database.
        
        Returns:
            List of InventoryTransaction objects
        """
        query = select(InventoryTransaction)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, transaction_id: int) -> InventoryTransaction | None:
        """
        Retrieve an inventory transaction by ID.
        
        Args:
            transaction_id: The inventory transaction ID
            
        Returns:
            InventoryTransaction object or None if not found
        """
        query = select(InventoryTransaction).where(InventoryTransaction.id == transaction_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, transaction_data: dict) -> InventoryTransaction:
        """
        Create a new inventory transaction.
        
        Args:
            transaction_data: Dictionary containing inventory transaction data
            
        Returns:
            Created InventoryTransaction object
        """
        transaction = InventoryTransaction(**transaction_data)
        self.db.add(transaction)
        await self.db.commit()
        await self.db.refresh(transaction)
        return transaction
    
    async def update(self, transaction_id: int, update_data: dict) -> InventoryTransaction | None:
        """
        Update an inventory transaction.
        
        Args:
            transaction_id: The inventory transaction ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated InventoryTransaction object or None if not found
        """
        transaction = await self.get_by_id(transaction_id)
        if not transaction:
            return None
        
        for key, value in update_data.items():
            setattr(transaction, key, value)
        
        await self.db.commit()
        await self.db.refresh(transaction)
        return transaction