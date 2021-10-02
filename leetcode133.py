'''
Think my solution works. This one had me stumped for about 15 minutes then the solution felt obvious.
'''
from graphs import Graph, Node


def graph_deep_copy(queue):
    graph_dict = {}
    while queue:
        vertex = queue.pop(0)
        graph_dict[vertex] = Node(vertex.value)
        for neighbor in vertex.neighbors:
            if neighbor not in queue and neighbor not in graph_dict.keys():
                queue.append(neighbor)

    for origin_node in graph_dict.keys():
        new_neighbors = [graph_dict[neighbor] for neighbor in origin_node.neighbors]
        graph_dict[origin_node].neighbors = new_neighbors

    return graph_dict.values()


example = [[10, 11, 12, 13], [[0, 1, 0, 1], [0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 1, 0]]]
example = Graph(example)
print(example)
copy = graph_deep_copy([example.nodes[0]])
new_graph = Graph()
new_graph.nodes = copy
print(new_graph)