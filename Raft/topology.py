import numpy as np

NODE_TO_NODE = 0
PEER_TO_NODE = 1
NODE_TO_PEER = 2


class Topology(object):

    def __init__(self, node_num, connected_peer_num):
        self.bw_matrix = np.zeros([node_num, node_num], dtype=float) # bandwidth matrix
        self.lt_matrix = np.zeros([node_num, node_num], dtype=float) # latency matrix

        self.inter_bw_matrix = np.zeros([connected_peer_num, node_num], dtype=float)
        self.inter_lt_matrix = np.zeros([connected_peer_num, node_num], dtype=float)

    def cal_delay(self, sender, receiver, msg_size: float, mode) -> float:
        delay = 0.0
        if msg_size == 0:
            if mode == PEER_TO_NODE:
                delay = self.inter_lt_matrix[sender][receiver]
            elif mode == NODE_TO_PEER:
                delay = self.inter_lt_matrix[receiver][sender]
            elif mode == NODE_TO_NODE:
                delay = self.lt_matrix[sender][receiver]
        else:
            if mode == PEER_TO_NODE:
                delay = self.inter_lt_matrix[sender][receiver] + msg_size / self.inter_bw_matrix[sender][receiver]
            elif mode == NODE_TO_PEER:
                delay = self.inter_lt_matrix[receiver][sender] + msg_size / self.inter_bw_matrix[receiver][sender]
            elif mode == NODE_TO_NODE:
                delay = self.lt_matrix[sender][receiver] + msg_size / self.bw_matrix[sender][receiver]

        return delay
