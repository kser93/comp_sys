def edges(data):
	edges = list()
	for v_i in data['vertices']:
		line = list()
		for v_j in data['vertices']:
			edge_ij = list(filter(
				lambda edge: edge['begin'] == v_i['id'] and edge['end'] == v_j['id'],
				data['edges']
			))
			line.append(edge_ij[0]['cost'] if edge_ij else None)
		edges.append(line)
	return edges	
	# for i in range(0, len(data['vertices']) + 1):
	# 	line = list()
	# 	for j in range(0, len(data['vertices']) + 1):
	# 		edge_ij = list(filter(
	# 			lambda edge: edge['begin'] == i and edge['end'] == j,
	# 			data['edges']
	# 		))
	# 		line.append(None if not edge_ij else edge_ij[0]['cost'])
	# 	edges.append(line)
	# return edges