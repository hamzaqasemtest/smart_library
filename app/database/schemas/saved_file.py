from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.database import database


class SavedFile(database.SqlAlchemyDatabaseConnection.Base):
    __tablename__ = 'saved_file'
    id = Column(Integer, primary_key=True)
    image_address = Column(JSON, nullable=False)
    audio_address = Column(String(255), nullable=True)
    document_address = Column(String(255), nullable=True)

    # Foreign key to associate a deployment with a user
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")

    def __repr__(self):
        return f"<SavedFile(image_address='{self.image_address}', audio_address='{self.audio_address}', user_id='{self.user_id}')>"
