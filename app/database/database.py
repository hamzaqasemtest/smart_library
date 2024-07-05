from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base


class SqlAlchemyDatabaseConnection():
    """
    Represents a connection to a SQL database using SQLAlchemy.

    Args:
        database_url (str): The URL of the database.

    Attributes:
        Base: The declarative base class for SQLAlchemy schemas.
        engine: The SQLAlchemy engine used for database connections.
        SessionLocal: The session factory for creating database sessions.
    """

    _instance = None
    Base = declarative_base()

    def __new__(cls, database_url):
        """
        Creates a new instance of SqlAlchemyDatabaseConnection if it doesn't exist.

        Args:
            database_url (str): The URL of the database.

        Returns:
            SqlAlchemyDatabaseConnection: The instance of SqlAlchemyDatabaseConnection.
        """
        if cls._instance is None:
            cls._instance = super(SqlAlchemyDatabaseConnection, cls).__new__(cls)
            cls._instance._initialize_connection(database_url)
        return cls._instance

    def _initialize_connection(self, database_url):
        """
        Initializes the database connection.

        Args:
            database_url (str): The URL of the database.
        """
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.metadata = MetaData()

    def get_session(self):
        """
        Creates and returns a new database session.

        Returns:
            Session: The database session.
        """
        return self.SessionLocal()

    def close_session(self, session):
        """
        Closes the given database session.

        Args:
            session (Session): The database session to close.
        """
        session.close()
