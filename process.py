import json
from logic.paths import paths
from logic.matrix import TSM
from logic.execution_time import execution_time
from pprint import pprint

from logic.vertices import vertices as upgrade_vertices
from logic.edges import edges as upgrade_edges

data = json.load(open('in.json', 'r'))

SM = TSM((data['vertices']))
pprint(SM, compact=True, width=100)
times = execution_time(data['vertices'])
tt = list((times['before'][i], times['after'][i]) for i in range(1, len(data['vertices'])))
for i in range(1, len(data['vertices'])):
	print('Vertex {}: before: {}\tafter: {}'.format(i, times['before'][i], times['after'][i]))
# # print(sorted(tt))