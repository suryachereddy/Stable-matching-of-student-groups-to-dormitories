from collections import defaultdict
from sdg import SDGroup


def QSO(G, D, merit, qs, bd):
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
    while itr < len(G)+1:
        mu_hat = {}
        new_G = dict(sorted(new_G.items()))
        mu_hat, R_hat = SDGroup(new_G, D, qg, bd)
        g_hat, idx = m(W_hat, merit)
        total_beds = sum(bd)
        total_other = 0
        for key, value in mu_hat.items():
            for v in value:
                total_other += qg[v]
        if W_hat == {} or (total_beds - total_other < qg[idx]):
            H += [(mu_hat, W_hat, R_hat)]
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
    for i, x in enumerate(sol):
        print(f"h: {i+1} H: {x}")
