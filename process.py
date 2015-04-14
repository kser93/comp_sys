import json
from pprint import pprint
from logic.threads import *
from logic.execution_time import thread_time


def process_and_display(threads, vertices, edges):
    time = [thread.get('time', thread_time(vertices, thread)) for thread in threads]
    result = connections_between_threads(edges, threads)
    pprint(threads)
    for line in result:
        for el in line:
            print('{} '.format(el if el is not None else '-'), end='')
        print()
    pprint(time)
    print()

data = json.load(open('in.json', 'r'))
unbalanced_threads = split_into_threads(**data)
process_and_display(unbalanced_threads, **data)

balanced_threads = balance(data['vertices'], unbalanced_threads)
process_and_display(balanced_threads, **data)