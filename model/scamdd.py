class SCAMDD():
    def __init__(self, data, eps = 0.6):
        self.r_data = list(data.columns)[:-1]
        self.n = len(data)
        self.data = data
        self.eps = eps
        self.delta = eps

    def free_max(self):
        self.delta_nclusters = []
        # find all maximal δ-nClusters in A
        for attr in self.r_data:
            ra = self.data[attr].sort_values()
            for p1 in range(self.n):
                for p2 in range(p1 + 1, self.n):
                    if self.dist_metric(ra.iloc[p1], ra.iloc[p2]) <= self.delta:
                        if p1 == 0 or p2 == self.n - 1 \
                            or self.dist_metric(ra.iloc[p1 - 1], ra.iloc[p2]) <= self.delta \
                            or self.dist_metric(ra.iloc[p1], ra.iloc[p2 + 1]) <= self.delta:
                            continue
                        self.delta_nclusters.append((ra.index[p1], ra.index[p2]))
                    

    def dist_metric(self, x1, x2):
        return (x1 - x2) ** 2


    def form_cand_LHSs(self):
        pass

    def find_RHSs(self):
        pass