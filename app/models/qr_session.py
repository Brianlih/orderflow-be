from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class QRSession(BaseModel):
    __tablename__ = "qr_sessions"
    
    table_id = Column(Integer, ForeignKey("tables.id"), nullable=False)
    session_token = Column(String(255), unique=True, nullable=False)
    status = Column(String(50), default="active")
    expires_at = Column(DateTime(timezone=True))
    last_activity = Column(DateTime(timezone=True))
    
    # Relationships
    table = relationship("Table", back_populates="qr_sessions")