def path_repr(path):
	return list(map(
		lambda x: x.id,
		path
	))

def group_repr(group):
	pass

def vertices_cost(path):
	return sum(list(map(lambda vertex: vertex.cost, path)))	

def edges_cost(path):
	edges_cost = 0
	for id in range(len(path) - 1):
		for descendant in path[id].descendants:
			if descendant['descendant'].id == path[id+1].id:
				edges_cost += descendant['cost']
				break
	return edges_cost

def total_cost(path):
	return vertices_cost(path) + edges_cost(path)

def is_not_generated(paths):
	for path in paths:
		if not path[-1].is_end():
			return True
	return False

def paths(vertices):
	start_vertices = list(filter(lambda vertex: vertex.is_start(), vertices))
	paths = list(map(lambda x: [x], start_vertices)) # paths initialize by start vertices
	while is_not_generated(paths):
		for path in paths:
			count_of_descendants = path[-1].count_of_descendants()
			if count_of_descendants == 0:
				continue
			elif count_of_descendants == 1:
				new_path = path + [path[-1].descendants[0]['descendant']]
				paths.append(new_path)
				paths.remove(path)
			elif count_of_descendants > 1:
				for descendant in path[-1].descendants:
					new_path = path + [descendant['descendant']]
					paths.append(new_path)
				paths.remove(path)					
	return sorted(paths)

def groups(paths):
	"""group paths by first and last vertices"""
	keys = set()
	for path in paths:
		keys.add((path[0].id, path[-1].id))
	groups = dict(zip(
		list(keys),
		[[]]*len(keys)
	))
	for path in paths:
		buf = groups[(path[0].id, path[-1].id)] + [path]
		groups[(path[0].id, path[-1].id)] = buf
	return groups