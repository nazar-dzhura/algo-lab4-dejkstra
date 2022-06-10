def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    path.append(start_node)

    print(f"Shortest path value: {format(shortest_path[target_node])}")
    print(" -> ".join(reversed(path)))