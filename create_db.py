from stpa_prototype.database import init_db, db_session
from stpa_prototype.models import *
import stpa_prototype

init_db()
stpa_prototype.user_datastore.create_user(email='user2', password='user2')
stpa_prototype.user_datastore.create_user(email='0', password='0')
db_session.commit()

user0 = User.query.filter_by(email='0').first()


project1 = Project('project1', 'project 1 description', user0)
project2 = Project('project2', 'project 1 description', user0)
project1.users.append(User.query.filter_by(email='user2').first())

db_session.add(project1)
db_session.commit()
db_session.add(project2)

db_session.commit()

