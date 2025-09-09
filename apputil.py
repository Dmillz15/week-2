import numpy as np


# update/add code below ...

def ways(n: int):
    combos = []
    for nickels in range(n // 5 + 1):
        pennies = n - 5 * nickels
        combos.append((pennies, nickels))
    return combos
ways(100)

names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])

def lowest_score(names, scores): 
    idx = np.argmin(scores)   # index of the minimum score
    return names[idx]

print(lowest_score(names, scores))

def sort_names(names, scores):
    sorted_idx = np.argsort(scores)[::-1]
    return list(names[sorted_idx])

print(sort_names(names, scores))