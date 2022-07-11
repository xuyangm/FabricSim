import numpy as np


class Topology(object):

    def __init__(self, node_num, bwm, ltm):
        self.bw_matrix = np.zeros([node_num, node_num], dtype=float)  # bandwidth matrix
        self.lt_matrix = np.zeros([node_num, node_num], dtype=float)  # latency matrix
        for i in range(node_num):
            for j in range(node_num):
                self.bw_matrix[i][j] = bwm[i][j]
                self.lt_matrix[i][j] = ltm[i][j]

    def cal_delay(self, sender, receiver, msg_size: float) -> float:
        if msg_size == 0:
            delay = self.lt_matrix[sender][receiver]
        else:
            delay = self.lt_matrix[sender][receiver] + msg_size / self.bw_matrix[sender][receiver]

        return delay
