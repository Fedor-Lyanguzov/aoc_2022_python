with open("input.py") as file:
    l = file.read().strip().split('\n')
from string import ascii_letters
d = {l:i for i, l in enumerate(ascii_letters, 1)}
def f(x):
    l = len(x)//2
    a = set(x[:l])
    b = set(x[l:])
    return list(a.intersection(b))[0]
print(sum(d[x] for x in map(f, l)))
def f2(x):
    a, b, c = x
    return list(set(a).intersection(set(b)).intersection(set(c)))[0]
print(sum(d[x] for x in map(f2, zip(l[::3],l[1::3],l[2::3]))))
