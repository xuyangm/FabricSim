import random
from event_manager import *

FOLLOWER = 0
CANDIDATE = 1
LEADER = 2
UNKNOWN = -1


class Orderer(object):
    """
    Orderer
    - Order transactions
    - Generate blocks
    """

    def __init__(self, id):
        self.min_election_timeout = 150  # ms
        self.max_election_timeout = 300

        self.id = id
        self.state = FOLLOWER
        self.term = 0
        self.leader = UNKNOWN
        self.vote = 0
        self.voted = False

    def get_election_timeout_event(self, clock: float) -> Event:
        e = Event()
        e.nid = self.id
        e.timestamp = clock + float(random.randint(self.min_election_timeout, self.max_election_timeout)) / 1000.0
        e.etype = ELECTION_TIMEOUT
        return e


class Peer(object):
    """
    Peer
    - Generate endorsements
    """

    def __init__(self, id):
        self.id = id


class Client(object):
    """
    Client
    - Generate transactions
    """

    def __init__(self, id):
        self.id = id