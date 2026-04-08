from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from src.config.config import settings
from pathlib import Path
import os,sys
from src.database.base import Base
import ssl

ssl_context = ssl.create_default_context()

engine = create_async_engine(
    settings.DATA_BASE,
    echo=True,
    connect_args={
        "ssl": ssl_context
    }
)

async_session = sessionmaker(
    engine, class_=AsyncSession,
    expire_on_commit=False
)