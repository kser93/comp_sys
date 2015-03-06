class Vertex(object):
	"""Vertex of algorithm graph-scheme"""

	def __init__(self, vertex):
		"""pre-constructor from JSON"""
		self.id = vertex['id']
		self.cost = vertex['cost']
		self.ascendants = vertex.get('ascendants', list())
		self.descendants = vertex.get('descendants', list())
		self.operator = vertex.get('operator', None)

	def __iter__(self):
		"""non-recursive dictifier"""
		yield ('id', self.id)
		yield ('cost', self.cost)
		yield ('operator', self.operator)
		yield (
			'descendants',
			list(map(
				lambda x: dict(
					cost=x['cost'],
					descendant=x['descendant'].id),
				self.descendants
			))
		)

	def __lt__(self, other):
		"""comparison of vertices by id"""
		return self.id < other.id

	def __repr__(self):
		"""non-recursive object printing"""
		return str(dict(self))

	def is_start(self):
		return len(self.ascendants) is 0

	def is_end(self):
		return len(self.descendants) is 0		

	def count_of_descendants(self):
		return len(self.descendants)