import random
from QSO import QSO
from tqdm import tqdm  # progress bar

bd = [0, 589, 119, 144, 248, 289, 11, 15,
      466, 806, 214, 770]  # index 0 is not used
n = 4000  # number of student
D = 11  # number of dorms
group_max = 5
qso_frequency = {}
refuge_frequency = {}
for itr in tqdm(range(1, 103+1)):

    groups = {}
    qg = [0]
    merit = {}
    n_new = n
    while n_new > 0:
        # max number of students in a group
        randomvalue = random.randint(1, group_max)
        if n_new-randomvalue < 0:
            qg.append(n)
            n_new = 0
        else:
            qg.append(randomvalue)
            n_new -= randomvalue

    # generate student groups
    visited = set()
    all = set(range(1, D+1))
    for i in range(1, len(qg)):
        # randomly choose dorm preferences
        dorm_pref = list(range(1, D+1))
        random.shuffle(dorm_pref)
        groups[i] = dorm_pref

    # generate merit scores
    merits = list(range(1, len(qg)))
    # ranomly shuffle merit scores
    random.shuffle(merits)
    for i in range(0, len(merits)):
        merit[i+1] = merits[i]  # randomly assign merit score
    result = QSO(groups, D, merit, qg, bd)
    number_of_qso = len(result)
    qso_frequency[number_of_qso] = qso_frequency.get(number_of_qso, 0) + 1
    number_of_refuge = len(result[1][2])  # only the first solution
    refuge_frequency[number_of_refuge] = refuge_frequency.get(
        number_of_refuge, 0) + 1

    groups.clear()
    merit.clear()
    # print generated data
print(qso_frequency)
print(refuge_frequency)
# save generated data to file
with open('qso_frequency.txt', 'w') as f:
    for key, value in qso_frequency.items():
        f.write("%s %s" % (key, value))
        f.write("\n")
with open('refuge_frequency.txt', 'w') as f:
    for key, value in refuge_frequency.items():
        f.write("%s %s" % (key, value))
        f.write("\n")
