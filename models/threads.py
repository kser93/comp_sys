def trepr(thread):
	return list(map(
		lambda x: x.id,
		thread
	))

def total_cost(thread):
	vertices_cost = sum(list(map(lambda vertex: vertex.cost, thread)))
	edges_cost = 0
	for id in range(len(thread) - 1):
		for descendant in thread[id].descendants:
			if descendant['descendant'].id == thread[id+1].id:
				edges_cost += descendant['cost']
				break
	return vertices_cost + edges_cost

def is_not_generated(threads):
	for thread in threads:
		if not thread[-1].is_end():
			return True
	return False

def threads(vertices):
	start_vertices = list(filter(lambda vertex: vertex.is_start(), vertices))
	threads = list(map(lambda x: [x], start_vertices)) # threads initialize by start vertices
	while is_not_generated(threads):
		for thread in threads:
			count_of_descendants = thread[-1].count_of_descendants()
			if count_of_descendants == 0:
				continue
			elif count_of_descendants == 1:
				new_thread = thread + [thread[-1].descendants[0]['descendant']]
				threads.append(new_thread)
				threads.remove(thread)
			elif count_of_descendants > 1:
				for descendant in thread[-1].descendants:
					new_thread = thread + [descendant['descendant']]
					threads.append(new_thread)
				threads.remove(thread)					
	return sorted(threads)

def group_threads(threads):
	"""group threads by first and last vertices"""
	keys = set()
	for thread in threads:
		keys.add((thread[0].id, thread[-1].id))
	groups = dict(zip(
		list(keys),
		[[]]*len(keys)
	))
	for thread in threads:
		buf = groups[(thread[0].id, thread[-1].id)] + [thread]
		groups[(thread[0].id, thread[-1].id)] = buf
	return groups