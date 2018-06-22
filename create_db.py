import stpa_prototype
from stpa_prototype.database.database import init_db, db_session
from stpa_prototype.database.models import *
from stpa_prototype.project_management.vcs import *

init_db()
# stpa_prototype.user_datastore.create_user(email='user2', password='user2')
# stpa_prototype.user_datastore.create_user(email='0', password='0')
# db_session.commit()

# user0 = User.query.filter_by(email='0').first()

#
# project1 = Project('project1', 'project 1 description', user0)
# init_db_repo(project1.id)
# project_db.init_db()
# create_and_commit_master(project.id)
# project2 = Project('project2', 'project 1 description', user0)
# project1.users.append(User.query.filter_by(email='user2').first())
#
# db_session.add(project1)
# db_session.commit()
# db_session.add(project2)
#
# db_session.commit()

