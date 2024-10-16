from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query

from sqlalchemy import Column, Integer, String, Boolean, DateTime,JSON
from sqlalchemy.sql import func
from .settings import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    email = Column(String(100), unique=True, index=True)
    age = Column(Integer)



class MasterAuthentication(Base):
    __tablename__ = "mas_authentication"

    auth_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, index=True, nullable=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    username = Column(String(100), nullable=True)
    phone = Column(String(15), nullable=True)
    is_active = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    doc_status = Column(String(30), nullable=True)
    last_login = Column(DateTime, nullable=True)
    date_joined = Column(DateTime, server_default=func.now())
    role_id = Column(String(100), nullable=True)
    permission_id = Column(JSON, nullable=True)
    comp_id = Column(String(20), nullable=True)
    registration_id = Column(String(100), nullable=True)
    created_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    created_by = Column(String(100), nullable=True)
    updated_by = Column(String(100), nullable=True)