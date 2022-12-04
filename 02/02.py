


with open("input.py") as file:
    l = [x.split() for x in file.read().strip().split('\n')]

d = {
    ("A", "X"): 1+3,
    ("A", "Y"): 2+6,
    ("A", "Z"): 3+0,
    ("B", "X"): 1+0,
    ("B", "Y"): 2+3,
    ("B", "Z"): 3+6,
    ("C", "X"): 1+6,
    ("C", "Y"): 2+0,
    ("C", "Z"): 3+3,
    }
d2 = {
    ("A", "X"): 3+0,
    ("A", "Y"): 1+3,
    ("A", "Z"): 2+6,
    ("B", "X"): 1+0,
    ("B", "Y"): 2+3,
    ("B", "Z"): 3+6,
    ("C", "X"): 2+0,
    ("C", "Y"): 3+3,
    ("C", "Z"): 1+6,
    }
        
print(sum(map(lambda x: d2[tuple(x)], l)))
