

GENERATE_TX = 0
RECEIVE_TX = 1
GENERATE_ENDORSED_TX = 2
RECEIVE_ENDORSED_TX = 3
GENERATE_BLOCK = 4
RECEIVE_BLOCK = 5


class Event(object):

    def __init__(self, etype, ts) -> None:
        self.etype = etype
        self.timestamp = ts


class EventManager(object):
    """
    Use a queue to manage events
    """

    def __init__(self) -> None:
        self.event_pool = []

    def append_event(self, e):
        self.event_pool.append(e)

    def get_event(self):
        return self.event_pool.pop()