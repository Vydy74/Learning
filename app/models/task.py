from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.models import *

class Task(Base):
    __tablename__="tasks"
    __table_args__={"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, nullable=True)
    complited = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship("User", back_populates="tasks")
