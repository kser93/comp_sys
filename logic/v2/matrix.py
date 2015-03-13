def sequence(data):
	matrix = list()
	extension = list()
	for i in range(len(data['vertices'])):
		line = list(map(
			lambda x: x[i],
			data['edges']
		))
		line = list(x if x is not None else 0 for x in line)
		matrix.append(line)
		extension.append(data['vertices'][i]['cost'])
		# print('{} || {}'.format(line, extension[-1]))
	return dict(
		matrix=matrix,
		extension=extension
	)