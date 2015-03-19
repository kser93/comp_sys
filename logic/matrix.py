from logic.paths import paths
from pprint import pprint
from functools import reduce
from logic.paths import *

def transitive(vertices):
	vr = range(len(vertices))
	return [[1 if paths(vertices, start=[i+1], finish=[j+1]) else 0 for j in vr] for i in vr]

# def incompatible(vertices, seq):
# 	LOL = list(filter(lambda x: x['function']['outcoming'] is '+', vertices))
# 	for CLO in LOL:
# 		branches = [[y] + [i + 1 for i, x in enumerate(list(zip(*seq))[y-1]) if x] for y in CLO['outcoming']]
# 		BI = list(reduce(set.intersection, [set(branch) for branch in branches]))
# 		pprint(paths(vertices, start=[vertices.index(CLO)+1], finish=[min(BI)] if BI else None))