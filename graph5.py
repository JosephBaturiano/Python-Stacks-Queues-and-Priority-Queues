from graph4 import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

print("\n", nodes["london"])

print("\n", graph)
