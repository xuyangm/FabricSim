SIM_TIME = 86400  # s
NODES_NUM = 6  # NODES_NUM = PEERS_NUM + ORDERERS_NUM
CLIENT_NUM = 1
PEER_NUM = 2
ORDERER_NUM = 3
BANDWIDTH_MATRIX = [[20, 20, 20, 20, 20, 20],
                    [20, 20, 20, 20, 20, 20],
                    [20, 20, 20, 20, 20, 20],
                    [20, 20, 20, 20, 20, 20],
                    [20, 20, 20, 20, 20, 20],
                    [20, 20, 20, 20, 20, 20]]  # MB
LATENCY_MATRIX = [[15, 15, 15, 15, 15, 15],
                    [15, 15, 15, 15, 15, 15],
                    [15, 15, 15, 15, 15, 15],
                    [15, 15, 15, 15, 15, 15],
                    [15, 15, 15, 15, 15, 15],
                    [15, 15, 15, 15, 15, 15]]  # ms
TPS = 200  # transaction arrival per second
TSIZE = 2  # KB
