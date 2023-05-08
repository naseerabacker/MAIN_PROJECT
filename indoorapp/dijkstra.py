def shortest_path(graph, node1, node2):

    print(graph)
    print("graphhhhhhhhhhhhhhhhh")
    print(node1)
    print("node111111111111111111111")
    print(node2)
    print("node2222222222222222222222222")
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []

#
# graph = {}
# #
# graph[1] = {2, 5}
# graph[2] = {1, 3, 5}
# graph[3] = {2, 4}
# graph[4] = {3, 5, 6}
# graph[5] = {1, 2, 4}
# graph[6] = {4}
#
# print(type(graph))
#
# d=dict()
#
#
#
#
#
# print(graph)
#
# g={1: {2}, 2: {1, 4}, 3: {4}, 4: {2, 3, 5}, 5: {4}}
# s=shortest_path(g,3,1)
# print(s)

# print(s)