#!/usr/bin/python3

import grpc
import order_service_pb2_grpc
from concurrent import futures

from Raft.event_manager import *
from Raft.node import *
from Raft.topology import *
from config import *


class OrdererByRaft(order_service_pb2_grpc.OrdererByRaft):

    def __init__(self):
        self.max_message_length = 90000000
        self.addr_port_pair = "127.0.0.1:50051"

        self.clock = 0
        self.event_manager = EventManager()
        self.nodes = []
        for i in range(NODES_NUM):
            self.nodes.append(Node(id=i))
        self.topo = Topology(NODES_NUM)

        # Generate initial ELECTION_TIMEOUT events
        for n in self.nodes:
            self.event_manager.insert_event(n.get_election_timeout_event(self.clock))

    def GetBlock(self, request, context):
        send_clock = request.send_timestamp
        msg_size = request.size
        sender = request.sender
        receiver = request.receiver

        target_clock = send_clock + self.topo.cal_delay(sender, receiver, msg_size, PEER_TO_NODE)

        while self.clock < target_clock and self.event_manager.is_empty():
            e = self.event_manager.get_event()
            if e.etype == ELECTION_TIMEOUT:
                self.trigger_election_timeout(e)
            else:
                pass
            self.clock = e.timestamp

    def trigger_election_timeout(self, e: Event):
        if not self.nodes[e.nid].voted:
            self.nodes[e.nid].term += 1  # increase the term
            self.nodes[e.nid].vote += 1  # vote for itself
            self.nodes[e.nid].state = CANDIDATE  # Follower/Candidate -> Candidate
            # reset election timer
            election_timeout_event = self.nodes[e.nid].get_election_timeout_event(e.timestamp)
            self.event_manager.insert_event(election_timeout_event)
            # send RequestVote to other nodes
            for n in self.nodes:
                if n.id != e.nid:
                    ts = e.timestamp + self.topo.cal_delay(e.nid, n.id, 0.0, NODE_TO_NODE)
                    new_event = Event(nid=n.id, etype=REQUEST_VOTE, timestamp=ts)
                    self.event_manager.insert_event(new_event)

        elif self.nodes[e.nid].vote > 0:
            election_timeout_event = self.nodes[e.nid].get_election_timeout_event(e.timestamp)
            self.event_manager.insert_event(election_timeout_event)

    def run(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=1), options=[
            ('grpc.max_send_message_length', self.max_message_length),
            ('grpc.max_receive_message_length', self.max_message_length),
        ])
        order_service_pb2_grpc.add_OrdererByRaftServicer_to_server(self, server)

        server.add_insecure_port(self.addr_port_pair)
        server.start()
        server.wait_for_termination()


if __name__ == "__main__":
    orderers = OrdererByRaft()
    orderers.run()
