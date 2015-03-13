import json

def seq(filename):
	data = json.load(open(filename, 'r'))
	vertices = data['vertices']
	edges = data['edges']
	seq_matrix = dict()
	for vertex_i in vertices:
		i = vertex_i['id']
		seq_matrix[i] = dict()
		for vertex_j in vertices:
			j = vertex_j['id']
			current_edge = list(filter(
				lambda edge: edge['begin'] == j and edge['end'] == i,
				edges
			))
			if len(current_edge) == 0:
				seq_matrix[i][j] = 0
			else:
				seq_matrix[i][j] = current_edge[0]['cost']

	with open('out/seq.txt', 'w') as fil:
		for i in range(1, len(vertices) + 1):
			fil.write(str(i).ljust(5))
			for j in range(1, len(vertices) + 1):
				el = seq_matrix[i][j]
				fil.write(str(el).ljust(3) if el != 0 else '-  ')
			fil.write(' || {}\n'.format(vertices[i-1]['cost']))
		fil.write('\n     ')
		for i in range(1, len(vertices) + 1):
			fil.write(str(i).ljust(3))

	with open('out/seq.txt', 'r') as fil:
		for line in fil:
			print(line, end='')
		print()