from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.dbs.qr_session.model import QRSession
from typing import List


class QRSessionMgmt:
    """Database management operations for QR sessions."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_active(self) -> List[QRSession]:
        """
        Retrieve all QR sessions from the database.
        
        Returns:
            List of QRSession objects
        """
        query = select(QRSession)
        result = await self.db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, session_id: int) -> QRSession | None:
        """
        Retrieve a QR session by ID.
        
        Args:
            session_id: The QR session ID
            
        Returns:
            QRSession object or None if not found
        """
        query = select(QRSession).where(QRSession.id == session_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
    
    async def create(self, session_data: dict) -> QRSession:
        """
        Create a new QR session.
        
        Args:
            session_data: Dictionary containing QR session data
            
        Returns:
            Created QRSession object
        """
        session = QRSession(**session_data)
        self.db.add(session)
        await self.db.commit()
        await self.db.refresh(session)
        return session
    
    async def update(self, session_id: int, update_data: dict) -> QRSession | None:
        """
        Update a QR session.
        
        Args:
            session_id: The QR session ID
            update_data: Dictionary containing update data
            
        Returns:
            Updated QRSession object or None if not found
        """
        session = await self.get_by_id(session_id)
        if not session:
            return None
        
        for key, value in update_data.items():
            setattr(session, key, value)
        
        await self.db.commit()
        await self.db.refresh(session)
        return session