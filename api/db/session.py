from typing import AsyncGenerator  # noqa: D104

from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from ..settings import get_settings
from .create_db import engine

settings = get_settings()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Get sesion fron SessionLocal.

    :yield: session object
    """
    async with SessionLocal() as session:
        yield session
