from sqlalchemy import Column, Integer, String
from stpa_prototype.database import Base
from datetime import datetime
from sqlalchemy import Boolean, DateTime


class Goal(Base):
    __tablename__ = 'system_goals'
    id = Column('goal_id', Integer, primary_key=True)
    title = Column(String(60))
    text = Column(String)
    vcs_check = Column(Boolean)
    pub_date = Column(DateTime)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.vcs_check = False
        self.pub_date = datetime.utcnow()


class Hazard(Base):
    __tablename__ = 'system_hazard'
    id = Column('hazard_id', Integer, primary_key=True)
    title = Column(String(60))
    text = Column(String)
    vcs_check = Column(Boolean)
    pub_date = Column(DateTime)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.vcs_check = False
        self.pub_date = datetime.utcnow()
