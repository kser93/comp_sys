import json
from logic.paths import paths
from logic.matrix import *
from pprint import pprint

data = json.load(open('in.json', 'r'))
SM = transitive((data['vertices']))
pprint(SM, compact=True, width=100)
# ILOM - incompatible logical operator matrix
all_paths = paths(data['vertices'])
# incompatible(data['vertices'], SM)
# pprint(paths(data['vertices'], start=[13], finish=[13]))