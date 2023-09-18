#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """Represents a user."""

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # Add a relationship with Place class
    places = relationship("Place", backref="user")
