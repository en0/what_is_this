from mylib import WeightedGraph, PriorityQueue
from heapq import heappush, heappop
from math import inf


def mine(r: str, g: WeightedGraph):
    """

    I think the time complexity is O(n*e)
    where n is the number of vertices and e is the number of edges

    """
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


def prim(r, g: WeightedGraph):
    """This is the real prim's algorithm"""

    visited = set()
    heap = PriorityQueue()
    costs = dict()
    parent = dict()

    for v in g:
        cost = 0 if r == v else inf
        costs[v] = cost
        heap.push(v, cost)

    while heap:
        v = heap.pop()
        if v in visited:
            continue
        visited.add(v)
        for w, a, _ in g.get_edges(v):
            if w < costs[a] and a not in visited:
                costs[a] = w
                heap.push(a, w)
                parent[a] = (v, w)

    return [(c[1], p, c[0]) for p, c in parent.items()]


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

mine = sorted(mine("A", g), key=lambda x: x[0])
print("MINE:", sum([x[0] for x in mine]), mine)

prim = sorted(prim("A", g), key=lambda x: x[0])
print("PRIM:", sum([x[0] for x in prim]), prim)
