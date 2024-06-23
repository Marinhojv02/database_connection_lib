from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Database:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.engine = None
        self.SessionLocal = None

    def connect(self):
        try:
            self.engine = create_engine(
                f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
            )
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

            #MODELS
            from .user_model import UserModel
            
            Base.metadata.create_all(bind=self.engine)
            print("Connection to PostgreSQL DB successful")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def get_session(self):
        if self.SessionLocal is None:
            raise Exception("The database connection is not established. Call connect() first.")
        return self.SessionLocal()

    def close(self):
        if self.engine is not None:
            self.engine.dispose()
            print("Database connection closed")
