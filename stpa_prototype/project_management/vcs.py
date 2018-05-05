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
    index.commit('temp_text')


def get_repo(project_id):
    repo_path = join(os_path, str(project_id))
    repo = Repo(repo_path)
    assert not repo.bare
    return repo


#
# repo_path = join(os_path, str(1))
# repo = Repo(repo_path)
# master = repo.heads.master
# print repo.commit().name_rev
# git = repo.git
# int_i = 0
# for commit in repo.iter_commits():
#     print commit.name_rev
#     if int_i == 2:
#         git.checkout('master')
#     int_i += 1




# init_db_repo('5')
# create_and_commit_master('6')

# add_and_commit('6')

#
# repo_path = join(os_path, '1')
# repo = Repo(repo_path)
# master = repo.head.reference
# for item in list(repo.iter_commits()):
#     print item.message
#     print item.name_rev
# print master.log()


# assert not repo.bare
# print repo.is_dirty()
