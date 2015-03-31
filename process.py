import json
from logic.paths import find_paths
from logic.matrix import TSM
from logic.execution_time import all_vertices_time, threads_time
from logic.threads import elementary_threads
from pprint import pprint

from logic.upgrade_initial import upgrade_vertices, upgrade_edges

data = json.load(open('in.json', 'r'))

# old_data = json.load(open('in-old.json', 'r'))
# pprint(upgrade_vertices(old_data), compact=True, width=100)
# pprint(upgrade_edges(old_data), compact=True, width=100)

# pprint(find_paths(data['vertices'], start=[2, 3, 7], finish=[14, 23]))
# pprint(find_paths(data['vertices'], start=[2, 3, 7]))
# pprint(find_paths(data['vertices'], finish=[14, 23]))
# pprint(find_paths(data['vertices']))
#
# pprint(TSM(data['vertices']), compact=True, width=100)
# pprint(elementary_threads(data['edges']))
el_threads = dict(
    times=threads_time(data['vertices'], elementary_threads(data['edges'])),
    threads=elementary_threads(data['edges'])
)
pprint(el_threads)
# pprint(threads_time(data['vertices'], elementary_threads(data['edges'])))