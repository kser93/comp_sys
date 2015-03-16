def paths(vertices, **kwargs):
	start=kwargs.get('start', None)
	if start is None:
		start = [i + 1 for i, x in enumerate(vertices) if x in list(filter(lambda x: not x['incoming'], vertices))]
		paths = [[x] for x in start]
	elif type(start) is list:
		paths = [[x] for x in start]
	elif type(start) is int:
		start = [start]
		paths = [start]
	else:
		raise ValueError("Wrong arguments!")

	finish=kwargs.get('finish', None)
	if finish is None:
		finish = [i + 1 for i, x in enumerate(vertices) if x in list(filter(lambda x: not x['outcoming'], vertices))]
	elif type(finish) is list:
		pass
	elif type(finish) is int:
		finish = [finish]
	else:
		raise ValueError("Wrong arguments!")

	for path in paths:
		outcoming = vertices[path[-1]-1]['outcoming']
		if outcoming:
			paths += list(map(lambda x: path + [x], outcoming))
	condition = lambda path: path[0] in start and path[-1] in finish
	return sorted(list(filter(condition, paths)))