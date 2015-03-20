from logic.paths import paths
from pprint import pprint

def TSM(vertices):
	"""Returns a transitive sequence matrix for vertices structure"""
	vr = range(1, len(vertices))
	return [None] + [[None] + [1 if paths(vertices, start=[i], finish=[j]) else 0 for j in vr] for i in vr]

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