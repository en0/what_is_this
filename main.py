from mylib import WeightedGraph
from heapq import heappush, heappop


def find_mst(r: str, g: WeightedGraph):
    mst = []
    queue = []
    visited = set([r])

    def add_edge(n):
        for e in g.get_edges(n):
            if e[1] not in visited:
                heappush(queue, e)

    add_edge(r)

    while len(queue) > 0:
        e: tuple = heappop(queue)
        if e[1] in visited:
            continue
        visited.add(e[1])
        add_edge(e[1])
        mst.append(e)

    return mst


g = WeightedGraph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
g.add_vertex("G")

g.add_edge("A", "B", weight=3)
g.add_edge("A", "C", weight=4)
g.add_edge("A", "D", weight=5)
g.add_edge("B", "D", weight=1)
g.add_edge("C", "E", weight=3)
g.add_edge("C", "F", weight=6)
g.add_edge("C", "G", weight=4)
g.add_edge("D", "G", weight=3)
g.add_edge("E", "F", weight=4)

print(g)
print(find_mst("A", g))
