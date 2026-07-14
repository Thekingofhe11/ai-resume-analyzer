from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            print("Database connection successful!")
    except Exception as e:
        print("Database connection failed:", e)
