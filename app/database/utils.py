from pydantic import BaseModel, create_model
from typing import Type, Any
from sqlalchemy.orm import DeclarativeMeta


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def create_dto(model: Type[DeclarativeMeta]) -> Type[BaseModel]:
    """
    Dynamically create a Pydantic DTO from a SQLAlchemy model.
    """
    fields = {
        col.name: (col.type.python_type, ...)
        for col in model.__table__.columns
    }

    dto = create_model(
        f"{model.__name__}DTO",
        **fields,
        __config__=type('Config', (), {'orm_mode': True})
    )

    return dto
