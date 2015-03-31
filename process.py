import json
from logic.execution_time import threads_time
from logic.threads import elementary_threads, connections_between_threads
from logic.threads_merge import merge

data = json.load(open('in.json', 'r'))

el_threads = dict(zip(
    threads_time(data['vertices'], elementary_threads(data['edges'])),
    elementary_threads(data['edges'])
))
for line in connections_between_threads(data['edges'], merge(el_threads)):
    for el in line:
        print('{} '.format(0 if el is 0 else 1 if el is not None else '-'), end='')
    print()