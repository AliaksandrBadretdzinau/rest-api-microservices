import os

from sqlmodel import create_engine, SQLModel

sqlite_file_name = "database.db"
DATABASE_URI = os.getenv('DATABASE_URI')
# f"sqlite:///{sqlite_file_name}"

engine = create_engine(DATABASE_URI, echo=True)

def create_db_and_tables():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
