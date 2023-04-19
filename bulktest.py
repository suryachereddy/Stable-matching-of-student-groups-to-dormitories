import random
from QSO import QSO

bd = [598, 119, 144, 248, 289, 11, 15, 466, 806, 214, 770]

n = 15  # number of student
m = 11  # number of dorms

groups = {}
qg = [0]
merit = {}
while n > 0:
    randomvalue = random.randint(1, 5)
    if n-randomvalue < 0:
        qg.append(n)
        n = 0
    else:
        qg.append(randomvalue)
        n -= randomvalue

# generate student groups
visited = set()
all = set(range(1, m+1))
for i in range(1, len(qg)):
    # randomly choose dorm preferences
    intermediate = list(all - visited)

    if i == len(qg)-1 and intermediate != []:
        # make sure all dorms are visited
        random.shuffle(intermediate)
        dorm_pref = intermediate
        groups[i] = dorm_pref
        break
    else:
        dorm_pref = random.sample(range(1, m+1), random.randint(1, m))
        visited.update(dorm_pref)
    groups[i] = dorm_pref

# generate merit scores
merits = list(range(1, len(qg)))
# ranomly shuffle merit scores
random.shuffle(merits)
for i in range(0, len(merits)):
    merit[i+1] = merits[i]  # randomly assign merit score

# print generated data
print("Groups: ", groups)
print("Number of students in each group: ", qg)
print("Merit scores: ", merit)
