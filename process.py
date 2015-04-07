import json
from pprint import pprint
from logic.threads import *

data = json.load(open('in.json', 'r'))

threads = split_into_threads(**data)
result = connections_between_threads(data['edges'], threads)

pprint(threads)
for line in result:
    for el in line:
        print('{} '.format(el if el is not None else '-'), end='')
    print()