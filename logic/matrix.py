from logic.paths import paths
from pprint import pprint
from operator import itemgetter as it_g
from itertools import groupby

def TSM(vertices):
	"""Returns a transitive sequence matrix for vertices structure"""
	vr = range(len(vertices))
	return [[1 if paths(vertices, start=[i], finish=[j]) else 0 for j in vr] for i in vr]

def incompatible(vertices, seq):
	LOL = list(filter(lambda x: x['function']['outcoming'] is '+', vertices))
	LOLI = [i for i, x in enumerate(vertices) if x in LOL]
	for i in LOLI:

		branches = [seq[x] for x in vertices[i]['outcoming']]
		# branches = [seq[i-1] if i]
		pprint(branches, compact=True, width=100)
	# # pprint(list(set(x) for x in branches))
	# for branches in all_branches:
	# 	# BI = 
	# 	BI = list(set.intersection(*list(set(x) for x in branches)))
	# 	pprint(BI)
	
	# branches = [[y] + [i + 1 for i, x in enumerate(list(zip(*seq))[y-1]) if x] for y in CLO['outcoming']]
	# pprint(paths(vertices, start=[vertices.index(CLO)+1], finish=[min(BI)] if BI else None))