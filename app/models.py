from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from .database import Base


class User(Base):
    """
    Описывает модель пользователя в базе данных.

    Attributes:
        id (int): Уникальный идентификатор пользователя.
        full_name (str): Полное имя пользователя.
        email (str): Электронная почта пользователя.
        phone (str): Номер телефона пользователя.
        hashed_password (str): Хэшированный пароль пользователя.
        is_active (bool): Флаг активности пользователя.

    Returns:
        User
    """
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    full_name: str = Column(String, index=True)
    email: str = Column(String, unique=True, index=True)
    phone: str = Column(String, unique=True, index=True)
    hashed_password: str = Column(String)
    is_active: bool = Column(Boolean, default=True)


class Product(Base):
    """
    Описывает модель продукта в базе данных.

    Attributes:
        id (int): Уникальный идентификатор продукта.
        name (str): Название продукта.
        price (int): Цена продукта.
        created_at (datetime): Дата и время создания продукта.
        updated_at (datetime): Дата и время последнего обновления продукта.
        is_active (bool): Флаг активности продукта.

    Returns:
        Product
    """
    __tablename__ = "products"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, index=True)
    price: int = Column(Integer)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)
    updated_at: datetime = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active: bool = Column(Boolean, default=True)
