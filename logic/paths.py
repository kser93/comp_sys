def paths(vertices, **kwargs):
	"""
	Finding paths from list of 'start' vertices to list of 'finish' vertices
	Example: paths(vertices, start=[2,3,7], finish=[14,23])
	"""
	def outer_vertices(kind):
		missing = lambda x: 'incoming' if x is 'start' else 'outcoming' if x is 'finish' else None
		outer = list(filter(lambda vertex: not vertex[missing(kind)], vertices))
		return [i + 1 for i, x in enumerate(vertices) if x in outer]

	start=kwargs.get('start', None)
	finish=kwargs.get('finish', None)
	
	if start is None:
		start = outer_vertices('start')
	if finish is None:
		finish = outer_vertices('finish')
	if type(start) is not list or type(finish) is not list:
		raise ValueError("Wrong arguments!")

	paths = [[x] for x in start]

	for path in paths:
		outcoming = vertices[path[-1]-1]['outcoming']
		if outcoming:
			paths += list(map(lambda x: path + [x], outcoming))
	condition = lambda path: path[0] in start and path[-1] in finish and len(path) > 1
	return sorted(list(filter(condition, paths)))