

class Transaction(object):

    def __init__(self, tid, tsize, timestamp, sender):
        self.tid = tid
        self.tsize = tsize
        self.timestamp = timestamp
        self.sender = sender
