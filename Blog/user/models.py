from core.db import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean

class User(Base):
    __tablename__='user'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True)
    data = Column(DateTime)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

