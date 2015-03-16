import json
from logic.vertices import vertices as upgrade_vertices
from logic.edges import edges as upgrade_edges

print("This script allows you to input the initial data into the script. Please, follow instructions.")
vertices_number = int(input("How much vertices do you have? >"))
vertices = list()
for i in range(1, vertices_number + 1):
	print("Input data for vertex " + str(i))
	cost = int(input("\tInput cost of vertex " + str(i) + " >"))
	vertices.append(dict(id=i, cost=cost))

print("Now input edges.")
is_continue = True
edges = list()
while is_continue:
	begin = int(input("\tInput number of start vertex >"))
	end = int(input("\tInput number of final vertex >"))
	operator = input("\tInput operator of edge(+ or &)[default &] >")
	if operator is not '+':
		operator = '&'
	cost = int(input("\tInput cost of edge >"))
	edges.append(dict(begin=begin, end=end, operator=operator, cost=cost))
	buff = input("Put something to stop or press Enter to continue >")
	is_continue = len(buff) is 0

data = dict(vertices=vertices, edges=edges)
vertices = upgrade_vertices(data)
edges = upgrade_edges(data)

print("Generating initial JSON...")
with open('in.json', 'w') as fil:
	json.dump(dict(vertices=vertices, edges=edges), fil)
print("JSON generated successfully.")