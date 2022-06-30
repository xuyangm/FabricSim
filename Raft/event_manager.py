import bisect

ELECTION_TIMEOUT = 0
REQUEST_VOTE = 1


class Event(object):

    def __init__(self, nid, etype, timestamp) -> None:
        self.nid = nid
        self.etype = etype
        self.timestamp = timestamp

    def __lt__(self, other):
        return self.timestamp > other.timestamp


class EventManager(object):

    def __init__(self) -> None:
        self.event_pool = []

    def insert_event(self, e):
        bisect.insort_left(self.event_pool, e)

    def get_event(self):
        return self.event_pool.pop()

    def is_empty(self):
        return len(self.event_pool) == 0
