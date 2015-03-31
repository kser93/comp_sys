import json
from pprint import pprint

from logic.execution_time import threads_time
from logic.threads import elementary_threads
from logic.threads_merge import merge


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
el_threads = dict(zip(
    threads_time(data['vertices'], elementary_threads(data['edges'])),
    elementary_threads(data['edges'])
))
pprint(el_threads)
merge(el_threads)