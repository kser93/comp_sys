def sequence(data):
	matrix = list()
	for i in range(len(data['vertices'])):
		line = list(map(
			lambda x: x[i],
			data['edges']
		))
		line = list(0 if x is None else 1 for x in line)
		matrix.append(line)
	return matrix

def sequence_extended(data):
	matrix = sequence(data)
	extension = list()
	for i in range(len(data['vertices'])):
		extension.append(data['vertices'][i]['cost'])
	return dict(
		matrix=matrix,
		extension=extension
	)
