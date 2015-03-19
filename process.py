import json
from logic.paths import paths
from logic.matrix import TSM, incompatible
from pprint import pprint

data = json.load(open('in1.json', 'r'))
# pprint(data['vertices'], compact=True)
# print(len(data['vertices']))
# pprint(data['edges'], compact=True, width=100)
# print(len(data['edges']))

SM = TSM((data['vertices']))
pprint(SM, compact=True, width=100)
# ILOM - incompatible logical operator matrix
# all_paths = paths(data['vertices'])
# incompatible(data['vertices'], SM)
# pprint(paths(data['vertices'], start=[13], finish=[13]))