
with open("input.py") as file:
    f = file.read().strip().split('\n')

def convert(x):
    a, b = x.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')
    a1, a2, b1, b2 = map(int, [a1,a2,b1,b2])
    return ((a1, a2), (b1, b2))
pairs = list(map(convert, f))

def contains(a, b):
    a1, a2 = a
    b1, b2 = b
    return b1<=a1 and a2<=b2
print(sum(1 for a, b in pairs if contains(a, b) or contains(b, a)))

def overlap(a, b):
    a1, a2 = a
    b1, b2 = b
    return b1<=a1<=b2 or b1<=a2<=b2
print(sum(1 for a, b in pairs if overlap(a, b) or overlap(b, a)))
