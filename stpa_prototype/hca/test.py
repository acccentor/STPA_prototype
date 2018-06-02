class TestClass():
    list = []


def recursive(remaining_columns, path, result):
    if not remaining_columns:
        return path
    for payload in remaining_columns[0]:
        # path.append()
        # print 'path: ' + format(path)
        # print 'payload: ' + format(payload)
        # print 'result b: ' + format(result)
        # print 'remaining: ' + format(remaining_columns)
        # print 'remainging[1:]' + format(remaining_columns[1:])
        if not remaining_columns[1:]:
            result.append(recursive(remaining_columns[1:], path + [payload], result))
        else:
            recursive(remaining_columns[1:], path + [payload], result)
    return result

#
# def cross_join(pmvs):
#     project_db_session = ProjectDB(session['active_project_db']).get_project_db_session()
#     pmv_list = project_db_session.query(PMV).order_by(PMV.id.asc()).all()
#     x = 0
#     pmvv = []
#     for pmv in pmv_list:
#         if x == 0:
#             pmvv = pmv.pmvvs
#         else:
#
#     pmvv_list = project_db_session.query(PMVV).order_by(PMVV.id.asc()).all()
#     pmvv


print recursive([['hei', 'hello'],['ewfawef', 'woiejf'], ['1','2','3']], [],[])
