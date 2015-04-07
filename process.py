import json
from pprint import pprint
from logic.execution_time import threads_time
from logic.threads import connections_between_threads
from logic.threads_merge import merge_by_time
# from logic.threads_new import merge_by_edge_cost, merge_logical_branches
from logic.threads_new import merge_logical_branches, merge_by_edge_cost

data = json.load(open('in.json', 'r'))

el_threads = dict(zip(
    threads_time(data['vertices'], merge_by_edge_cost(data['vertices'], data['edges'])),
    merge_by_edge_cost(data['vertices'], data['edges'])
))

pprint(el_threads)
for line in connections_between_threads(data['edges'], merge_by_time(dict(el_threads))):
    for el in line:
        # print('{} '.format(el), end='')
        print('{} '.format(0 if el is 0 else el if el is not None else '-'), end='')
    print()

pprint(merge_by_time(dict(zip(
    threads_time(data['vertices'], merge_by_edge_cost(data['vertices'], data['edges'])),
    merge_by_edge_cost(data['vertices'], data['edges'])
))))

# pprint(merge_by_edge_cost(data['vertices']))
# pprint(merge_logical_branches(data['vertices']))