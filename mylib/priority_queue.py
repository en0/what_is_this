from heapq import heappush, heappop
from itertools import count


REMOVED_MEMBER = hash("<!REMOVED-MEMBER!>")


class PriorityQueue:
    def __init__(self):
        self._counter = count()
        self._heap = list()
        self._map = dict()

    def push(self, member, value):
        if member in self._map:
            self._remove_member(member)
        entry = [value, next(self._counter), member]
        heappush(self._heap, entry)
        self._map[member] = entry

    def pop(self):
        while self._heap:
            priority, order, member = heappop(self._heap)
            if member != REMOVED_MEMBER:
                del self._map[member]
                return member
        raise KeyError("Queue Empty")

    def get_priority(self, member):
        priority, _, _ = self._map[member]
        return priority

    def _remove_member(self, member):
        entry = self._map.pop(member)
        entry[-1] = REMOVED_MEMBER

    def __len__(self):
        return len(self._map)

    def __bool__(self):
        return len(self) > 0
