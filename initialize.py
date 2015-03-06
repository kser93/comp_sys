import json
print("This script allows you to input the initial data into the script. Please, follow instructions.")
vertices_number = int(input("How much vertices do you have? >"))
vertices = list()
for i in range(1, vertices_number + 1):
	print("Input data for vertice " + str(i))
	cost = int(input("\tInput cost of vertice " + str(i) + " >"))
	vertices.append(dict(id=i, cost=cost))

print("Now input edges.")
is_continue = True
edges = list()
while is_continue:
	begin = int(input("\tInput number of begin vertice >"))
	end = int(input("\tInput number of end vertice >"))
	operator = input("\tInput operator of edge(+ or &) >")
	cost = int(input("\tInput cost of edge >"))
	edges.append(dict(begin=begin, end=end, operator=operator, cost=cost))
	buff = input("Put something to stop or press Enter to continue >")
	is_continue = len(buff) is 0

print("Generating initial JSON...")
with open('in.json', 'w') as fil:
	json.dump(dict(vertices=vertices, edges=edges), fil, indent=4)
print("JSON generated successfully.")

data = json.dumps(dict(vertices=vertices, edges=edges), indent=4)
print(data)