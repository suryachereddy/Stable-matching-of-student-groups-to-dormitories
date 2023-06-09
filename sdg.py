
import copy
from collections import defaultdict


def SDGroup(Gprime, D, qg, bd):
    G = copy.deepcopy(Gprime)
    n = len(G) - 1
    matching = defaultdict(list)
    i = 1
    refuge = []
    c = True
    for i in G.keys():
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
    groups = {}
    groups[1] = [2, 1]  # preference list
    groups[2] = [2, 1]
    groups[3] = [1]
    groups[4] = [2, 1]
    qg = [None, 2, 1, 2, 1]
    bd = [None, 2, 2]
    D = 2
    matching, refuge = SDGroup(groups, D, qg, bd)
    # invert matching
    inter_inverted_matching = {
        value: key for key in matching for value in matching[key]}
    inverted_matching = [(value, inter_inverted_matching[value])
                         for value in inter_inverted_matching]
    print(f"matching: {inverted_matching} and refuge: {refuge}")
