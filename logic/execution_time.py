def execution_time(vertices):

	def functor(vertex):
		operator = vertex['function']['incoming']
		if operator is None:
			return 0
		precs = list(after[i] for i in vertex['incoming'])
		return\
			precs[0] if operator is 'E' else\
			max(precs) if operator is '&' else\
			min(precs) if operator is '+' else None

	before = [None]
	after = [None]
	for vertex in vertices[1:]:
		before.append(functor(vertex))
		after.append(before[-1] + vertex['cost'])
	return dict(before=before, after=after)