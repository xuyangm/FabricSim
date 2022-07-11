#!/usr/bin/python3

import numpy as np
from config import *
from event_manager import *
from node import Client, Peer, Orderer
from topology import Topology
from transaction import Transaction


def init_txs(tx_pool):
    n_tx = TPS * SIM_TIME
    times = np.random.randint(low=0, high=SIM_TIME, size=n_tx)
    times.sort()
    for i in range(n_tx):
        tx_pool.append(Transaction(tid=i, tsize=TSIZE, timestamp=times[i], sender=0))


def init_events(em: EventManager, tx_pool):
    for tx in tx_pool:
        ev = Event()



def run():
    clock = 0

    # initialize topology
    topo = Topology(NODES_NUM, BANDWIDTH_MATRIX, LATENCY_MATRIX)

    # initialize nodes
    clients = []
    peers = []
    orderers = []
    for i in range(CLIENT_NUM):
        clients.append(Client(id=i))
    for i in range(CLIENT_NUM, CLIENT_NUM+PEER_NUM):
        peers.append(Peer(id=i))
    for i in range(CLIENT_NUM+PEER_NUM, NODES_NUM):
        orderers.append(Orderer(id=i))

    # initialize transactions
    tx_pool = []
    init_txs(tx_pool)

    # initialize events
    event_manager = EventManager()
    init_events(event_manager)



if __name__ == "__main__":
    run()