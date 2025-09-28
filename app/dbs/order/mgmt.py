from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.order.model import Order
from typing import List


class OrderMgmt:
    """Database management operations for orders."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[Order]:
        """
        Retrieve all orders from the database.
        
        Returns:
            List of Order objects
        """
        query = select(Order)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, order_id: int) -> Order | None:
        """
        Retrieve an order by ID.
        
        Args:
            order_id: The order ID
            
        Returns:
            Order object or None if not found
        """
        query = select(Order).where(Order.id == order_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, order_data: dict) -> Order:
        """
        Create a new order.
        
        Args:
            order_data: Dictionary containing order data
            
        Returns:
            Created Order object
        """
        order = Order(**order_data)
        self.db.add(order)
        await self.db.commit()
        await self.db.refresh(order)
        return order
    
    async def update(self, order_id: int, update_data: dict) -> Order | None:
        """
        Update an order.
        
        Args:
            order_id: The order ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated Order object or None if not found
        """
        order = await self.get_by_id(order_id)
        if not order:
            return None
        
        for key, value in update_data.items():
            setattr(order, key, value)
        
        await self.db.commit()
        await self.db.refresh(order)
        return order