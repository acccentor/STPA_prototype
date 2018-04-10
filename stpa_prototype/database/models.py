from stpa_prototype.database.database import Base
from flask_security import UserMixin, RoleMixin

from sqlalchemy.orm import relationship, backref

from sqlalchemy import Boolean, DateTime, ForeignKey, Column, Integer, String
from datetime import datetime


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


# class User(Base):
#     __tablename__ = 'auth_user'
#     id = Column('goal_id', Integer, primary_key=True)
#     name = Column(String(128),  nullable=False)
#     password = Column(String(192),  nullable=False)
#
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password


# example User from https://pythonhosted.org/Flask-Security/quickstart.html
class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255))
    password = Column(String(255))
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    confirmed_at = Column(DateTime())
    roles = relationship('Role', secondary='roles_users',
                         backref=backref('users', lazy='dynamic'))
    projects = relationship('Project', secondary='project_users', backref=backref('projects', lazy='dynamic'))

# example Role from https://pythonhosted.org/Flask-Security/quickstart.html
class Role(Base, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))


class RolesUsers(Base):
    __tablename__ = 'roles_users'
    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
    role_id = Column('role_id', Integer(), ForeignKey('role.id'))


class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer(), primary_key=True)
    title = Column(String(80), unique=True)
    description = Column(String(255))
    users = relationship('User', secondary='project_users', backref=backref('users', lazy='dynamic'))

    def __init__(self, title, desc, user):
        self.title = title
        self.description = desc
        self.users.append(user)


class ProjectUsers(Base):
    __tablename__ = 'project_users'
    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
    project_id = Column('role_id', Integer(), ForeignKey('project.id'))
