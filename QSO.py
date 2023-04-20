from collections import defaultdict
from sdg import SDGroup
import copy


def QSO(G, D, merit, qg, bd):
    def m(G, merit):
        new_merit = {}
        for key, value in G.items():
            new_merit[key] = merit[key]
        if new_merit == {}:
            return [], None
        Keymax = max(new_merit, key=lambda x: new_merit[x])
        return G[Keymax], Keymax
    g_hat, idx = m(G, merit)
    W_hat = G.copy()
    W_hat.pop(idx)
    new_G = {idx: g_hat}
    H = []
    h = 1
    itr = 1
    while itr < len(qg):
        mu_hat = {}
        new_G = dict(sorted(new_G.items()))
        mu_hat, R_hat = SDGroup(new_G, D, qg, bd)
        g_hat, idx = m(W_hat, merit)
        total_beds = sum(bd)
        total_other = 0
        for key, value in mu_hat.items():
            for v in value:
                total_other += qg[v]

        if W_hat == {} or (total_beds - total_other) < qg[idx]:
            new_mu = copy.deepcopy(mu_hat)
            new_R = copy.deepcopy(R_hat)
            new_W = copy.deepcopy(W_hat)
            inter_inverted_mu = {
                value: key for key in new_mu for value in new_mu[key]}
            inverted_mu = [(value, inter_inverted_mu[value])
                           for value in inter_inverted_mu]
            H.append((inverted_mu, new_W, new_R))

            h += 1
        if W_hat != {}:
            W_hat.pop(idx)

        new_G.update({idx: g_hat})

        itr += 1
    return H


if __name__ == '__main__':
    groups = {}
    # groups are sorted by preference of merit

    groups[1] = [1, 2, 3, 4]  # (dorm preference list, merit)
    groups[2] = [1]
    groups[3] = [1, 2, 3, 4]
    groups[4] = [1, 2, 3, 4]
    groups[5] = [1, 2, 3, 4]
    qg = [0, 1, 2, 1, 1, 1]
    bd = [0, 2, 1, 1, 1]
    D = 2
    merit = {
        1: 1, 2: 5, 3: 4, 4: 3, 5: 2
    }
    sol = QSO(groups, D, merit, qg, bd)
    print(len(sol))
    for i, x in enumerate(sol):
        print(f"h: {i+1} H: {x}")
