import json
from logic.paths import paths
from logic.matrix import TSM
from logic.execution_time import execution_time
from pprint import pprint

data = json.load(open('in.json', 'r'))

SM = TSM((data['vertices']))
# pprint(SM, compact=True, width=100)
times = execution_time(data['vertices'])
for i in range(1, len(data['vertices'])):
	print('Vertex {}: before: {}\tafter: {}'.format(i, times['before'][i], times['after'][i]))