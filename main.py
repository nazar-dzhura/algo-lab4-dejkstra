from Algorhythms.Dijkstra.Graph import Graph
from Algorhythms.Dijkstra.dijkstra import dijkstra_algorithm
from Algorhythms.Dijkstra.printing import print_result

nodes = ["Lviv", "Kyiv", "Kharkiv", "London", "Rome", "Berlin", "Rivne", "Athens"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["Lviv"]["Kyiv"] = 5
init_graph["Lviv"]["London"] = 4
init_graph["Kyiv"]["Berlin"] = 1
init_graph["Kyiv"]["Kharkiv"] = 3
init_graph["Kharkiv"]["Rivne"] = 5
init_graph["Kharkiv"]["Athens"] = 4
init_graph["Athens"]["Rivne"] = 1
init_graph["Rome"]["Berlin"] = 2
init_graph["Rome"]["Athens"] = 2
graph = Graph(nodes, init_graph)
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Lviv")
print_result(previous_nodes, shortest_path, start_node="Lviv", target_node="Rivne")