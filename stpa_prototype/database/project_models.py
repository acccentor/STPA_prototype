from sqlalchemy import Boolean, DateTime, ForeignKey, Column, Integer, String
from datetime import datetime

from sqlalchemy.orm import relationship, backref

from stpa_prototype.database.database_project import ProjectDB


class Goal(ProjectDB.PBase):
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


class Hazard(ProjectDB.PBase):
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


class ControlAction(ProjectDB.PBase):
    __tablename__ = 'system_control_action'
    id = Column('control_action_id', Integer, primary_key=True)
    title = Column(String(60))
    text = Column(String)
    vcs_check = Column(Boolean)
    pub_date = Column(DateTime)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.vcs_check = False
        self.pub_date = datetime.utcnow()
        
        
class PMV(ProjectDB.PBase):
    __tablename__ = 'system_pmv'
    id = Column('pmv_id', Integer, primary_key=True)
    title = Column(String(60))
    text = Column(String)
    vcs_check = Column(Boolean)
    pub_date = Column(DateTime)
    pmvvs = relationship('PMVV', back_populates="pmv")

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.vcs_check = False
        self.pub_date = datetime.utcnow()


class PMVV(ProjectDB.PBase):
    __tablename__ = 'system_pmvv'
    id = Column('pmvv_id', Integer, primary_key=True)
    text = Column(String)
    vcs_check = Column(Boolean)
    pub_date = Column(DateTime)
    pmv_id = Column(Integer, ForeignKey('system_pmv.pmv_id'))
    pmv = relationship("PMV", back_populates="pmvvs")

    def __init__(self, text):
        self.text = text
        self.vcs_check = False
        self.pub_date = datetime.utcnow()
