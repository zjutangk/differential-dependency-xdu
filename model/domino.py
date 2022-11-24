import pandas as pd


class Domino:
    def __init__(self, data):
        self.attr_list = list(data.columns)[:-1]
        self.data = data[self.attr_list]
        self.m = len(self.attr_list)
        self.n = self.data.shape[0]
        
        self.delta_dist = None

    def run(self):
        RFDcs = {}
        self.delta_dist = self.get_distance_relation()
        for attr in self.attr_list:
            ordered_delta_dist = self.ordered_relation(attr)
            T = self.get_TRel(ordered_delta_dist[attr])
            


    def _dist(self, xi, yi):
        return self.data.iloc[xi] - self.data.iloc[yi];

    def get_distance_relation(self):
        delta_dist = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                delta_dist.append(self._dist(i, j))
        delta_dist = pd.DataFrame(delta_dist, columns=self.attr_list)
        return delta_dist
    
    def ordered_relation(self, attr):
        return self.data.sort_values(by=attr, ascending=False)
    
    def _get_next_smaller_beta(self, current_beta):
        
        return None

    
    def get_TRel(self, ordered_attr):
        T, T_beta = {}, {}
        beta = None
        for i in range(ordered_attr.shape[0]):
            if beta is not None:
                beta[i] = self._get_next_smaller_value(beta)  # type: ignore
    

