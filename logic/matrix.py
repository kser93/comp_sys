from logic.paths import find_paths


def TSM(V):
    """Returns a transitive sequence matrix for vertices structure"""
    return [[1 if find_paths(V, start=[i['id']], finish=[j['id']]) else 0 for j in V] for i in V]