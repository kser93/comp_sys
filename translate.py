import json
from logic.vertices import vertices as upgrade_vertices
from logic.edges import edges as upgrade_edges

data = json.load(open('in-old.json', 'r'))

vertices = upgrade_vertices(data)
edges = upgrade_edges(data)

with open('in1.json', 'w') as fil:
	json.dump(dict(vertices=vertices, edges=edges), fil)