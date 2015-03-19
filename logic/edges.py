def edges(data):
	edges = list()
	for i in range(0, len(data['vertices']) + 1):
		line = list()
		for j in range(0, len(data['vertices']) + 1):
			edge_ij = list(filter(
				lambda edge: edge['begin'] == i and edge['end'] == j,
				data['edges']
			))
			line.append(None if not edge_ij else edge_ij[0]['cost'])
		edges.append(line)
	return edges