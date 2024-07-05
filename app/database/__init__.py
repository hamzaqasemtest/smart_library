from app.database.database import SqlAlchemyDatabaseConnection
from app.database.schemas import *
from config import DB_DIALECT, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
from app.database.schemas.user import User
from app.database import database
from app.database.crud_base import CRUDBase
from app.database.utils import create_dto


database_url = f"{DB_DIALECT}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
sql_database_connection = SqlAlchemyDatabaseConnection(database_url)
sql_database_connection.Base.metadata.create_all(sql_database_connection.engine)

UserDTO = create_dto(User)
user_crud = CRUDBase(sql_database_connection, User, UserDTO)

if (sql_database_connection.get_session().query(User).count() == 0):
    q = user_crud.add(username='test', password_hash='test')
