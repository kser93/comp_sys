from pprint import pprint
from functools import reduce
from logic.paths import *

def sequence(edges):
	return [[x if x else 0 for x in line] for line in list(zip(*edges))]

def unweighted(sequence):
	return [[1 if x else 0 for x in line] for line in sequence]

def transitive(sequence):
	for i in range(len(sequence)):
		for j in range(len(sequence)):
			if sequence[i][j]:
				for k in range(j):
					sequence[i][k] = (sequence[i][j] and sequence[j][k]) or sequence[i][k]
	return sequence

def incompatible(vertices, seq):
	LOL = list(filter(lambda x: x['function']['outcoming'] is '+', vertices))
	for CLO in LOL:
		branches = [[y] + [i + 1 for i, x in enumerate(list(zip(*seq))[y-1]) if x] for y in CLO['outcoming']]
		BI = list(reduce(set.intersection, [set(branch) for branch in branches]))
		pprint(paths(vertices, start=[vertices.index(CLO)+1], finish=[min(BI)] if BI else None))