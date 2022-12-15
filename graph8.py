import networkx as nx
from graph4 import City, load_graph

graph = nx.nx_agraph.read_dot("roadmap.dot")
nodes, graph = load_graph("roadmap.dot", City.from_dict)
