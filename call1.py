import numpy as np
from dijkstra import dijkstra


class call1(object):
    path = []
    wt_matx = []
    wt_matx_real = []
    wt_matx_real1 = []

    def __init__(self, p, s, d, flow_type, min_rate, wt_matx, wt_matx_real, wt_matx_real1):
        self.p = p
        self.s = s
        self.d = d
        self.flow_type = flow_type
        self.min_rate = min_rate
        self.wt_matx = wt_matx
        self.wt_matx_real = wt_matx_real
        self.wt_matx_real1 = wt_matx_real1

    def execute(self):
        if self.flow_type == 2:
            dummy = np.divide(1, self.wt_matx)
            if self.min_rate == 0:
                dummy1 = dummy
            else:
                dummy1 = np.subtract(dummy, self.min_rate)
            dummy2 = dummy1 > 0
            dummy3 = np.multiply(dummy1, dummy2)
            with np.errstate(divide='ignore', invalid='ignore'):
                dummy4 = np.divide(1, dummy3)
            for i in range(0, self.p, 1):
                for j in range(0, self.p, 1):
                    # Could be an erroneous declaration of negative Inf
                    if dummy4[i][j] == -float('inf'):
                        dummy4[i][j] == float('inf')
            dij = dijkstra(self.s, self.d, dummy4)
            path = dij.execute()
            s2 = np.shape(path)[0]
            if s2 == 0:
                path = np.zeros((self.p))
            else:
                flow = np.zeros((self.p, self.p))
                for i in range(0, s2-1, 1):
                    flow[path[i], path[i+1]] = self.min_rate
                dummy5 = dummy-flow
                self.wt_matx = np.divide(1, dummy5)
                if s2 < self.p:
                    for j in range(s2, self.p, 1):
                        path = np.append(path, 0)
        else:
            dummy1 = np.divide(1, self.wt_matx_real1)
            print(dummy1)
            if self.min_rate == 0:
                dummy2 = dummy1
            else:
                dummy2 = np.subtract(dummy1 - self.min_rate)
            dummy3 = dummy2 > 0
            with np.errstate(divide='ignore', invalid='ignore'):
                dummy4 = np.divide(1, self.wt_matx)
            dummy5 = np.multiply(dummy4, dummy3)
            if self.min_rate == 0:
                dummy6 = dummy5
            else:
                dummy6 = np.subtract(dummy5, self.min_rate)
            dummy7 = dummy6 > 0
            dummy8 = np.multiply(dummy6, dummy7)
            with np.errstate(divide='ignore', invalid='ignore'):
                dummy9 = np.divide(1, dummy8)
            for i in range(0, self.p, 1):
                for j in range(0, self.p, 1):
                    if dummy9[i][j] == -float('inf'):
                        dummy9[i][j] == float('inf')
            print("dummy9")
            print dummy9
            dij = dijkstra(self.s, self.d, dummy9)
            path = dij.execute()
            s2 = np.shape(path)[0]
            if s2 == 0:
                path = np.zeros((self.p))
            else:
                flow = np.zeros((self.p, self.p))
                print flow
                for i in range(0, s2 - 1, 1):
                    print(path[i])
                    print(path[i+1])
                    print "k2"
                    print self.min_rate
                    print path[i]
                    print path[i+1]
                    flow[path[i], path[i+1]] = self.min_rate
                dummy10 = np.subtract(np.divide(1, self.wt_matx_real), flow)
                dummy11 = np.subtract(dummy1, flow)
                dummy12 = np.subtract(dummy4, flow)
                wt_matx_real = np.divide(1, dummy10)
                wt_matx_real1 = np.divide(1, dummy11)
                wt_matx = np.divide(1, dummy12)
                if s2 < self.p:
                    print(s2)
                    print(self.p)
                    print(path)
                    print("FISKER")
                    for j in range(s2, self.p, 1):
                        path = np.append(path, 0)
                    self.wt_matx = wt_matx
                    self.wt_matx_real = wt_matx_real
                    self.wt_matx_real1 = wt_matx_real1
        self.path = path
