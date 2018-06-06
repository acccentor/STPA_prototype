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
    # hca = relationship('HCA', secondary='hca_hazard', backref=backref('hca_table', lazy='dynamic'))

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
    hca = relationship('HCA', secondary='hca_pmvv', backref=backref('hca_table', lazy='dynamic'))

    def __init__(self, text):
        self.text = text
        self.vcs_check = False
        self.pub_date = datetime.utcnow()


class HCA(ProjectDB.PBase):
    __tablename__ = 'hca_table'
    id = Column('hca_id', Integer(), primary_key=True)
    # cah = relationship("Hazard", ForeignKey('system_hazard.id'))
    cah = relationship('Hazard', secondary='hca_hazard')
    cah_tl = relationship('Hazard', secondary='hca_hazard')
    cah_te = relationship('Hazard', secondary='hca_hazard')
    # cah_tl = relationship("Hazard")
    # cah_te = relationship("Hazard")
    ca_id = Column(Integer, ForeignKey('system_control_action.control_action_id'))
    ca = relationship("ControlAction", uselist=False)

    pmvvs = relationship("PMVV", secondary='hca_pmvv', backref=backref('system_pmvv', lazy='dynamic'))

    # ca = Column(Integer, ForeignKey('system_control_action.control_action_id'))
    # pmv = Column(Integer, ForeignKey('system_pmv.pmv_id'))

    def __init__(self, ca):
        self.ca_id = ca.id
        # self.pmvs = pmvs
        # self.pmvvs = pmvvs


class HCAHazard(ProjectDB.PBase):
    __tablename__ = 'hca_hazard'
    id = Column(Integer(), primary_key=True)
    hca_id = Column('hca_id', Integer(), ForeignKey('hca_table.hca_id'))
    hazard_id = Column('hazard_id', Integer(), ForeignKey('system_hazard.hazard_id'))


class HcaPmvv(ProjectDB.PBase):
    __tablename__ = 'hca_pmvv'
    id = Column(Integer(), primary_key=True)
    hca_id = Column('hca_id', Integer(), ForeignKey('hca_table.hca_id'))
    pmvv_id = Column('pmvv_id', Integer(), ForeignKey('system_pmvv.pmvv_id'))