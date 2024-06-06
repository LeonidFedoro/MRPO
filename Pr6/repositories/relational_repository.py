from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base_repository import BaseRepository

class RelationalRepository(BaseRepository):
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)

    def save(self, entity):
        session = self.Session()
        session.add(entity)
        session.commit()
        session.close()

    def get_by_id(self, entity_class, id):
        session = self.Session()
        entity = session.query(entity_class).filter_by(id=id).first()
        session.close()
        return entity

    # Другие методы для работы с базой данных

