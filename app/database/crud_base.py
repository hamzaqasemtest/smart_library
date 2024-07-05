from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Type, TypeVar, Generic, Optional, Union
from pydantic import BaseModel
from app.database.database import SqlAlchemyDatabaseConnection
from app.database.utils import singleton


@singleton
class CRUDBase:
    M = TypeVar('M')
    T = TypeVar('T', bound=BaseModel)

    def __init__(self, db: SqlAlchemyDatabaseConnection, model: Type[M], dto: Type[T]):
        self.db = db
        self.model = model
        self.dto = dto

    def add(self, **kwargs) -> T:
        session: Session = self.db.get_session()
        new_instance = self.model(**kwargs)
        try:
            session.add(new_instance)
            session.commit()
            return self.dto.from_orm(new_instance)
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get(self, identifier: Union[int, str]) -> Optional[T]:
        session: Session = self.db.get_session()
        try:
            if isinstance(identifier, int):
                instance = session.query(self.model).filter(self.model.id == identifier).first()
            elif isinstance(identifier, str):
                instance = session.query(self.model).filter(self.model.username == identifier).first()
            else:
                return None

            if instance:
                return self.dto.from_orm(instance)
            else:
                return None
        except SQLAlchemyError as e:
            raise e
        finally:
            session.close()

    def update(self, identifier: Union[int, str], **kwargs) -> Optional[T]:
        session: Session = self.db.get_session()
        try:
            if isinstance(identifier, int):
                instance = session.query(self.model).filter(self.model.id == identifier).first()
            elif isinstance(identifier, str):
                instance = session.query(self.model).filter(self.model.username == identifier).first()
            else:
                return None

            if instance:
                for key, value in kwargs.items():
                    setattr(instance, key, value)
                session.commit()
                return self.dto.from_orm(instance)
            else:
                return None
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete(self, identifier: Union[int, str]) -> bool:
        session: Session = self.db.get_session()
        try:
            if isinstance(identifier, int):
                instance = session.query(self.model).filter(self.model.id == identifier).first()
            elif isinstance(identifier, str):
                instance = session.query(self.model).filter(self.model.username == identifier).first()
            else:
                return False

            if instance:
                session.delete(instance)
                session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
