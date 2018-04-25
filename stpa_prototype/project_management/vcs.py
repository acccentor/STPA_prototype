import os

from git import Repo, osp

join = osp.join

os_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../resources/db/projects"))


def init_db_repo(project_id):
    repo_path = join(os_path, str(project_id))
    assert Repo.init(repo_path).__class__ is Repo


def create_and_commit_master(project_id):
    repo_path = join(os_path, str(project_id))
    repo = Repo(repo_path)
    assert not repo.bare
    index = repo.index
    index.add(['project.db'])
    index.commit('create_and_commit_master')
    repo.create_head('master')


def add_and_commit(project_id):
    repo_path = join(os_path, str(project_id))
    repo = Repo(repo_path)
    assert not repo.bare
    index = repo.index
    index.add(['project.db'])
    index.commit()



# init_db_repo('5')
# create_and_commit_master('6')

# add_and_commit('6')
# repo_path = join(os_path, '6')
# repo = Repo(repo_path)
# assert not repo.bare
# print repo.is_dirty()
