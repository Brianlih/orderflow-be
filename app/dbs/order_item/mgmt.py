from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.order_item.model import OrderItem
from typing import List


class OrderItemMgmt:
    """Database management operations for order items."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[OrderItem]:
        """
        Retrieve all order items from the database.
        
        Returns:
            List of OrderItem objects
        """
        query = select(OrderItem)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, order_item_id: int) -> OrderItem | None:
        """
        Retrieve an order item by ID.
        
        Args:
            order_item_id: The order item ID
            
        Returns:
            OrderItem object or None if not found
        """
        query = select(OrderItem).where(OrderItem.order_item_id == order_item_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, order_item_data: dict) -> OrderItem:
        """
        Create a new order item.
        
        Args:
            order_item_data: Dictionary containing order item data
            
        Returns:
            Created OrderItem object
        """
        order_item = OrderItem(**order_item_data)
        self.db.add(order_item)
        await self.db.commit()
        await self.db.refresh(order_item)
        return order_item
    
    async def update(self, order_item_id: int, update_data: dict) -> OrderItem | None:
        """
        Update an order item.
        
        Args:
            order_item_id: The order item ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated OrderItem object or None if not found
        """
        order_item = await self.get_by_id(order_item_id)
        if not order_item:
            return None
        
        for key, value in update_data.items():
            setattr(order_item, key, value)
        
        await self.db.commit()
        await self.db.refresh(order_item)
        return order_item