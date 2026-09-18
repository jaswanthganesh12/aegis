from sqlalchemy.ext.asyncio import(AsyncSession, async_sessionmaker,create_async_engine)
from src.config import settings
from sqlalchemy import text


engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    async with AsyncSessionLocal()as session:
        yield session


async def check_database_connection():
    async with engine.connect() as connection:
        await connection.execute(text("SELECT 1"))