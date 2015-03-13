def edges(data):
	edges = list()
	for i in range(1, len(data['vertices']) + 1):
		line = list()
		for j in range(1, len(data['vertices']) + 1):
			line.append(None)
			for edge in data['edges']:
				if edge['begin'] == i and edge['end'] == j:
					line[-1] = edge['cost']
					break
		edges.append(line)
	return edges