import json
from logic.paths import find_paths
from logic.matrix import TSM
from logic.execution_time import execution_time
from pprint import pprint

from logic.upgrade_initial import upgrade_vertices, upgrade_edges

data = json.load(open('in.json', 'r'))

# times = execution_time(data['vertices'])
# tt = list((times['before'][i], times['after'][i]) for i in range(1, len(data['vertices'])))
# for i in range(1, len(data['vertices'])):
# print('Vertex {}: before: {}\tafter: {}'.format(i, times['before'][i], times['after'][i]))

# old_data = json.load(open('in-old.json', 'r'))
# pprint(upgrade_vertices(old_data), compact=True, width=100)
# pprint(upgrade_edges(old_data), compact=True, width=100)

pprint(find_paths(data['vertices'], start=[2, 3, 7], finish=[14, 23]))
pprint(find_paths(data['vertices'], start=[2, 3, 7]))
pprint(find_paths(data['vertices'], finish=[14, 23]))
pprint(find_paths(data['vertices']))
#
# pprint(TSM(data['vertices']), compact=True, width=100)