import json
import logic.v2.matrix as matrix

filename = 'in.json'
data = json.load(open(filename, 'r'))

vertices = data['vertices']
edges = data['edges']

# paths = paths(vertices)
# groups = groups(paths)
seq_matr = matrix.sequence(data)
# matr.save_seq(seq_matrix)

# # for path in sorted(paths):
# # 	print(path_repr(path))

# for key in sorted(groups.keys()):
# 	print('\n{}'.format(key))
# 	for path in sorted(groups[key], key=lambda path: edges_cost(path)):
# 		print(
# 			str(path_repr(path)).ljust(25),
# 			"vertex cost = {}".format(vertices_cost(path)).ljust(20),
# 			"edges cost = {}".format(edges_cost(path)).ljust(20),
# 			"total cost = {}".format(total_cost(path)).ljust(20)
# 		)

# # target = max(paths, key=lambda path: edges_cost(path))
# # print(
# # 	str(path_repr(target)).ljust(25),
# # 	"edges cost = {}".format(edges_cost(target)).ljust(20)
# # )

# # выделение нити максимальной длины и свертка графа