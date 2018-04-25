from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


class ProjectDB:
    PBase = declarative_base()

    def __init__(self, project_id):
        path = 'sqlite:///resources/db/projects/{}/project.db'.format(project_id)
        self.project_id = project_id
        self.engine = create_engine(path, convert_unicode=True)
        self.project_db_session = scoped_session(sessionmaker(autocommit=False,
                                                      autoflush=False,
                                                      bind=self.engine))
        # self.PBase.query = self.project_db_session.query_property()

    def init_db(self):
        import stpa_prototype.database.project_models
        ProjectDB.PBase.metadata.create_all(bind=self.engine)

    def get_project_db_session(self):
        return self.project_db_session
