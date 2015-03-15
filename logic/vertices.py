def connections(data, vertex_id, target='outcoming'):
	if target in ('incoming', 'outcoming'):
		points = ('begin', 'end') if target is 'outcoming' else ('end', 'begin')
		edges = list(filter(
			lambda x: x[points[0]] == vertex_id,
			data['edges']
		))
		edges_id = list(map(
			lambda x: x[points[1]],
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
	else:
		raise ValueError("target must be incoming or outcoming connections")

def vertices(data):
	vertices = list()
	for raw_vertex in data['vertices']:
		outc = connections(data, raw_vertex['id'], 'outcoming')
		inc = connections(data, raw_vertex['id'], 'incoming')
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
	return vertices