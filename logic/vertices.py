def connections(data, vertex, target):
	if target not in ('incoming', 'outcoming'):
		raise ValueError("target must be incoming or outcoming connections")

	first = lambda target: 'begin' if target is 'outcoming' else 'end'
	last = lambda target: 'end' if target is 'outcoming' else 'begin'
	edges = list(filter(
		lambda x: x[first(target)] == vertex,
		data['edges']
	))
	edges_id = list(map(
		lambda x: x[last(target)],
		edges
	))
	if not edges_id:
		edges_id = None
		func = None
	elif len(edges_id) == 1:
		func = 'E'
	else:
		func = edges[0]['operator']
	return dict(
		target=edges_id,
		function=func
	)

def vertices(data):
	vertices = list()
	for raw_vertex in data['vertices']:
		inc = connections(data, raw_vertex['id'], 'incoming')
		outc = connections(data, raw_vertex['id'], 'outcoming')
		vertices.append(
			dict(
				cost=raw_vertex['cost'],
				incoming=inc['target'],
				outcoming=outc['target'],
				function=dict(
					incoming=inc['function'],
					outcoming=outc['function']
				)
			)
		)
	return [None] + vertices