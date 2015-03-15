def paths(vertices):
	start_vertices = list(filter(lambda x: not x['incoming'], vertices))
	paths = list(map(lambda x: [vertices.index(x)], start_vertices)) # paths initialize by start vertices
	while is_not_generated(vertices, paths):
		for path in paths:
			next_vertices = vertices[path[-1]]['outcoming']
			if next_vertices:
				for next in next_vertices:
					new_path = path + [next - 1]
					paths.append(new_path)
				paths.remove(path)
				break
	for path in paths:
		paths[paths.index(path)] = list(map(lambda x: x+1, path))
	return sorted(paths)

def groups(paths):
	"""group paths by first and last vertices"""
	keys = set()
	for path in paths:
		keys.add((path[0], path[-1]))
	groups = dict(zip(
		list(keys),
		[[]]*len(keys)
	))
	for path in paths:
		buf = groups[(path[0], path[-1])] + [path]
		groups[(path[0], path[-1])] = buf
	return groups

def is_not_generated(vertices, paths):
	for path in paths:
		if vertices[path[-1]]['outcoming']:
			return True
	return False

def vertices_cost(path):
	return sum(list(map(lambda vertex: vertex.cost, path)))	

def edges_cost(path):
	edges_cost = 0
	for id in range(len(path) - 1):
		edges_cost += list(filter(
			lambda descendant: descendant['descendant'].id == path[id+1].id,
			path[id].descendants
		))[0]['cost']
	return edges_cost

def total_cost(path):
	return vertices_cost(path) + edges_cost(path)