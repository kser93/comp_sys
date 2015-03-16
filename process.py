import json
from logic.paths import *
from logic.matrix import *
from pprint import pprint

data = json.load(open('in.json', 'r'))
SM = transitive(unweighted(sequence(data['edges'])))
# ILOM - incompatible logical operator matrix
# pprint(paths(data['vertices'], start=[2,3,7], finish=[14,23]))
all_paths = paths(data['vertices'])
incompatible(data['vertices'], SM)