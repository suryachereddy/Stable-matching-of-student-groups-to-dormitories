
from collections import defaultdict


def SDGroup(G, D, qg, bd):
    n = len(G) - 1
    matching = defaultdict(list)
    i = 1
    refuge = []
    c = True
    while i < n+1:
        if G[i] != []:
            currpref = G[i]
            c = False
        dcurr = currpref[0] if currpref != [] else None
        while dcurr != None and c == False:
            total_other = 0

            if matching.get(dcurr) != []:
                for group in matching[dcurr]:
                    total_other += qg[group]
            if bd[dcurr] - total_other >= qg[i]:
                matching[dcurr] += [i]
                c = True
            else:
                G[i].pop(0)
                dcurr = G[i][0] if G[i] != [] else None
        if c == False:
            refuge += [i]
        i += 1
    return matching, refuge


if __name__ == '__main__':
    groups = [None]*(4+1)
    groups[1] = [2, 1]  # preference list
    groups[2] = [2, 1]
    groups[3] = [1]
    groups[4] = [1, 2]
    qg = [None, 2, 1, 2, 1]
    bd = [None, 2, 2]
    D = 2
    print(SDGroup(groups, D, qg, bd))
