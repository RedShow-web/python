from random import random

lst = [1, 8, 9, 1, 1, 2, 3, 5, 6, 5, 8, 9, 8, 1, 2]

used = set()
unique = [x for x in lst if x not in used and (used.add(x) or True)]
print(unique)

