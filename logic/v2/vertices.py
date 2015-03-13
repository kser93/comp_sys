def connections(edges, vertex_id, target='outcoming'):
	if target in ('incoming', 'outcoming'):
		modifier = 'begin' if target is 'outcoming' else 'end'
		return list(filter(
			lambda x: x[modifier] == vertex_id,
			edges
		))
	else:
		raise ValueError("target must be incoming or outcoming edges")

def vertices(data):

	vertices = list()
	for raw_vertex in data['vertices']:

		out_edges = connections(data['edges'], raw_vertex['id'], 'outcoming')
		if len(out_edges) == 0:
			out_func = None
			outcoming = None
		else:
			out_func = out_edges[0]['operator']
			outcoming = list(map(
				lambda x: x['end'],
				out_edges
			))

		in_edges = connections(data['edges'], raw_vertex['id'], 'incoming')
		if len(in_edges) == 0:
			in_func = None
			incoming = None
		else:
			in_func = in_edges[0]['operator']
			incoming = list(map(
				lambda x: x['begin'],
				in_edges
			))

		vertices.append(
			dict(
				cost=raw_vertex['cost'],
				incoming=incoming,
				outcoming=outcoming,
				function=dict(
					incoming=in_func,
					outcoming=out_func
				)
			)
		)

	return vertices