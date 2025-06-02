from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

Base = declarative_base()

class QueueEntry(Base):
    __tablename__ = 'queue_entries'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    username = Column(String)
    join_time = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    dryer_number = Column(Integer)

class Database:
    def __init__(self):
        if os.path.exists('dryer_queue.db'):
            os.remove('dryer_queue.db')
        self.engine = create_engine('sqlite:///dryer_queue.db')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_to_queue(self, user_id: int, username: str, dryer_number: int):
        entry = QueueEntry(user_id=user_id, username=username, dryer_number=dryer_number)
        self.session.add(entry)
        self.session.commit()

    def get_queue_info(self, dryer_number: int):
        return self.session.query(QueueEntry).filter_by(dryer_number=dryer_number, is_active=True).order_by(QueueEntry.join_time).all()
