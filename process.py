import json
from models.vertex import Vertex
from logic.vertices import *
from logic.paths import *
from logic.matrix import *

filename = 'in.json'

data = json.load(open(filename, 'r'))

vertices = vertices(data)
paths = paths(vertices)
groups = groups(paths)

# for key in sorted(groups.keys()):
# 	print(key)
# 	for path in sorted(groups[key], key=lambda path: edges_cost(path)):
# 		print(
# 			str(prepr(path)).ljust(25),
# 			"vertex cost = {}".format(vertices_cost(path)).ljust(20),
# 			"edges cost = {}".format(edges_cost(path)).ljust(20),
# 			"total cost = {}".format(total_cost(path)).ljust(20)
# 		)
# 	print('\n')

target = max(paths, key=lambda path: edges_cost(path))
print(
	str(path_repr(target)).ljust(25),
	"edges cost = {}".format(edges_cost(target)).ljust(20)
)

seq(filename)

# выделение нити максимальной длины и свертка графа