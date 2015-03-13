from models.vertex import Vertex

def vertices(data):
	vertices = list(Vertex(vertex) for vertex in data['vertices'])

	for vertex in vertices:
		out_edges = list(filter(lambda x: x['begin'] == vertex.id , data['edges']))
		in_edges = list(filter(lambda x: x['end'] == vertex.id , data['edges']))
		if len(out_edges) > 0:
			vertex.operator = out_edges[0]['operator']

		ascendant_identifiers = list(map(lambda x: x['begin'], in_edges))
		descendant_identifiers = list(map(lambda x: x['end'], out_edges))
		descendant_costs = list(map(lambda x: x['cost'], out_edges))
		descendant_vertices = list(filter(lambda x: x.id in descendant_identifiers, vertices))
		descendants = list(zip(descendant_vertices, descendant_costs))

		vertex.descendants = list(map(lambda x: dict(zip(['descendant', 'cost'], x)), descendants))
		vertex.ascendants = list(filter(lambda x: x.id in ascendant_identifiers, vertices))
	return vertices