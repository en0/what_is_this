class WeightedGraph:
    """
        Weighted Graph backed by an adjacency matrix
    """

    def __init__(self):
        self._matrix = []
        self._vertex_list = []
        self._vertex_map = {}

    def add_vertex(self, v):
        index = len(self._vertex_list)
        self._vertex_list.append(v)
        self._vertex_map[v] = index
        for edges in self._matrix:
            edges.append(None)
        self._matrix.append([None] * len(self._vertex_list))

    def get_vertices(self) -> list:
        return self._vertex_list

    def add_edge(self, v, u, weight):
        v_index = self._vertex_map[v]
        u_index = self._vertex_map[u]
        self._matrix[v_index][u_index] = weight
        self._matrix[u_index][v_index] = weight

    def add_directed_edge(self, v, u, weight):
        v_index = self._vertex_map[v]
        u_index = self._vertex_map[u]
        self._matrix[v_index][u_index] = weight

    def get_weight(self, v, u) -> int:
        v_index = self._vertex_map[v]
        u_index = self._vertex_map[u]
        return self._matrix[v_index][u_index]

    def get_adjacent_vertices(self, v) -> list:
        v_index = self._vertex_map[v]
        result = []
        for u_index in range(self.count()):
            if self._matrix[v_index][u_index] is not None:
                result.append(self._vertex_list[u_index])
        return result

    def get_edges(self, v) -> dict:
        ret = list()
        for u in self.get_adjacent_vertices(v):
            ret.append((self.get_weight(v, u), u, v))
        return ret

    def count(self) -> int:
        return len(self._vertex_list)

    def __str__(self):
        """This is not very flexible"""

        # TODO: Make this auto size and whatnot

        sb = ["   " + " ".join("{0:2}".format(str(_)) for _ in self._vertex_list)]
        v_index = 0

        for vertex in self._matrix:
            line = [str(self._vertex_list[v_index])]
            v_index += 1
            for edge in vertex:
                line.append("{0:2}".format(" -" if edge is None else edge))
            sb.append(" ".join(line))
        return "\n".join(sb)
