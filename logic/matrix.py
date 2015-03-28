from logic.paths import paths
from pprint import pprint

def TSM(V):
	"""Returns a transitive sequence matrix for vertices structure"""
	return [[1 if paths(V, start=[i['id']], finish=[j['id']]) else 0 for j in V] for i in V]

# def incompatible(vertices, seq):
# 	LOL = list(filter(lambda x: x and x['function']['outcoming'] is '+', vertices))
# 	LOLI = [i for i, x in enumerate(vertices) if x in LOL]
# 	for index in LOLI:
# 		out = vertices[index]['outcoming']
# 		# pprint(out)
# 		branches = [[y] + [i for i, x in enumerate(seq[y]) if x] for y in out]
# 		# pprint(branches, compact=True, width=100)
# 		BI = list(set.intersection(*list(set(x) for x in branches)))
# 		pprint(branches)
# 		pprint(paths(vertices, start=[index], finish=[min(BI) if BI else None]))