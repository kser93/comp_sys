def seq(data):
	vertices = data['vertices']
	edges = data['edges']
	matrix = dict()
	for vertex_i in vertices:
		i = vertex_i['id']
		matrix[i] = dict()
		for vertex_j in vertices:
			j = vertex_j['id']
			current_edge = list(filter(
				lambda edge: edge['begin'] == j and edge['end'] == i,
				edges
			))
			matrix[i][j] = 0 if len(current_edge) == 0 else current_edge[0]['cost']
		matrix[i]['cost'] = vertices[i-1]['cost']
	return matrix

def save_seq(matrix):
	with open('out/seq.txt', 'w') as fil:
		for i in range(1, len(matrix) + 1):
			fil.write(str(i).ljust(5))
			for j in range(1, len(matrix) + 1):
				el = matrix[i][j]
				fil.write(str(el).ljust(3) if el != 0 else '-  ')
			fil.write(' || {}\n'.format(matrix[i]['cost']))
		fil.write('\n     ')
		for i in range(1, len(matrix) + 1):
			fil.write(str(i).ljust(3))
