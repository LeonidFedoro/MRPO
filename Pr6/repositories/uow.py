from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class UnitOfWork:
    def __init__(self):
        self.engine = create_engine('sqlite:///dating_app.db')
        self.Session = sessionmaker(bind=self.engine)

    def __enter__(self):
        self.session = self.Session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()
