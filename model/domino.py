import pandas as pd


class Domino:
    def __init__(self, data):
        self.attr_list = list(data.columns)[:-1]
        self.data = data[self.attr_list]
        self.m = len(self.attr_list)
        self.n = self.data.shape[0]
        
        self.delta_dist = None
        self.T=None

    def run(self):
        RFDcs = {}
        self.delta_dist = self.get_distance_relation()
        for attr in self.attr_list:
            ordered_delta_dist = self.ordered_delta(attr)
            self.delta_dist=ordered_delta_dist
            T = self.get_TRel(attr)
            


    def _dist(self, xi, yi):
        return abs(self.data.iloc[xi] - self.data.iloc[yi])

    def get_distance_relation(self):
        delta_dist = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                delta_dist.append(self._dist(i, j))
        delta_dist = pd.DataFrame(delta_dist, columns=self.attr_list)
        return delta_dist
    
    def ordered_delta(self, attr):
        return self.delta_dist.sort_values(by=attr, ascending=True)
    
    def _get_next_smaller_beta(self, xi,attr):
        for i in range(0,xi):
            if self.delta_dist.iloc[xi-i-1][attr]<self.delta_dist.iloc[xi][attr]
                return self.delta_dist.iloc[xi-i-1][attr]
        return 0

    def _dominate(self,xi,attr,l):
        f=0
        if len(l)==0:
            return 1
        for i in range(len(l)):
            for k in self.attr_list:
                    if l.iloc[i][k]>xi[k]:
                        return 0
                    if l.iloc[i][k]<xi[k]:
                        f=1
        if f:
            return 1
        else:
            return 0

    def get_TRel(self, attr):
        #? 这边瞎jb写的
        beta=self.delta_dist.iloc[-1][attr]
        n=len(self.delta_dist)
        T=dict(beta)
        for i in range(len(self.delta_dist)):
            beta_=self._get_next_smaller_beta(n-i,attr)
            if beta_<beta:
                beta=beta_
                T[beta] = []
            if self._dominate(self.delta_dist.iloc[n-i],attr,T[beta]):
                T[beta].append(self.delta_dist.iloc[n-i])






    

