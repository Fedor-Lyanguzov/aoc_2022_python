
with open('input') as file:
    field = list(map(lambda x: list(map(int, x)), file.read().strip().split('\n')))

visible = set()

for i in range(len(field)):
    m = -1
    for j in range(len(field)):
        if field[i][j]>m:
            m = field[i][j]
            visible.add((i, j))

for i in range(len(field)):
    m = -1
    for j in range(len(field)-1, -1, -1):
        if field[i][j]>m:
            m = field[i][j]
            visible.add((i, j))

for j in range(len(field)-1, -1, -1):
    m = -1
    for i in range(len(field)):
        if field[i][j]>m:
            m = field[i][j]
            visible.add((i, j))

for j in range(len(field)-1, -1, -1):
    m = -1
    for i in range(len(field)-1, -1, -1):
        if field[i][j]>m:
            m = field[i][j]
            visible.add((i, j))

print(len(visible))

def scenic_score(field, mi, mj):
    n = len(field)
    m = len(field[0])
    s = 1
    k = 0
    i = mi+1
    while not (i==n or field[i][mj]>=field[mi][mj]):
        k += 1
        i += 1
    if not i==n:
        k += 1
    s *= k
    k = 0
    i = mi-1
    while not (i==-1 or field[i][mj]>=field[mi][mj]):
        k += 1
        i -= 1
    if not i==-1:
        k += 1
    s *= k
    k = 0
    j = mj+1
    while not (j==m or field[mi][j]>=field[mi][mj]):
        k += 1
        j += 1
    if not j==n:
        k += 1
    s *= k
    k = 0
    j = mj-1
    while not (j==-1 or field[mi][j]>=field[mi][mj]):
        k += 1
        j -= 1
    if not j==-1:
        k += 1
    s *= k
    return s

print(max(scenic_score(field, i, j) for i in range(len(field)) for j in range(len(field[0]))))
