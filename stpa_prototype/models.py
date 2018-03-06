from sqlalchemy import Column, Integer, String
from stpa_prototype.database import Base
from datetime import datetime
from sqlalchemy import Boolean, DateTime


class Goals(Base):
    __tablename__ = 'system_goals'
    id = Column('todo_id', Integer, primary_key=True)
    title = Column(String(60))
    text = Column(String)
    vcs_check = Column(Boolean)
    pub_date = Column(DateTime)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.vcs_check = False
        self.pub_date = datetime.utcnow()
