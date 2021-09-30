from pandas import DataFrame


class Node:
    def __init__(self, value=None, neighbors=None):
        if neighbors is None:
            neighbors = []
        self.value = value
        self.neighbors = neighbors


class Graph:
    def __init__(self, graph_repr=None):
        if graph_repr is None:
            self.nodes = []
        else:
            self.read_adj_matrix(graph_repr[0], graph_repr[1])

    def read_adj_matrix(self, values, adj_matrix):
        self.nodes = []
        for value in values:
            self.nodes.append(Node(value))

        for i, row in enumerate(adj_matrix):
            for j, is_adj in enumerate(row):
                if is_adj:
                    self.nodes[i].neighbors.append(self.nodes[j])

    def adj_matrix(self):
        adj_mat = []
        for node in self.nodes:
            row = []
            for possible_neighbor in self.nodes:
                if possible_neighbor in node.neighbors:
                    row.append(1)
                else:
                    row.append(0)
            adj_mat.append(row)

        return adj_mat

    def values(self):
        return [node.value for node in self.nodes]

    def __repr__(self):
        df = DataFrame(self.adj_matrix())
        df.set_axis(self.values(), axis=1, inplace=True)
        df.set_axis(self.values(), axis=0, inplace=True)
        return str(df)


example = [[10, 11, 12, 13], [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]]

