from math import dist

with open('input') as file:
    cmds = file.read().strip().split('\n')

d = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (1, 0),
    'D': (-1, 0),
}

def walk(cmds):
    for cmd in cmds:
        cmd, v = cmd.split()
        v = int(v)
        cmd = d[cmd]
        for _ in range(v):
            yield cmd

def sign(x):
    if x==0:
        return 0
    return x//abs(x)

visited = {(0,0)}
head = (0,0)
tail = (0,0)
for i, j in walk(cmds):
    hi, hj = head
    hi += i
    hj += j
    head = hi, hj
    if dist(head, tail)>2**0.5:
        ti, tj = tail
        tj += sign(hj-tj)
        ti += sign(hi-ti)
        tail = ti, tj
        visited.add(tail)
print(len(visited))

rope = [(0,0)]*10
visited = {(0,0)}
for i, j in walk(cmds):
    hi, hj = rope[0]
    hi += i
    hj += j
    rope[0] = hi, hj
    for i, (head, tail) in enumerate(zip(rope, rope[1:]), 1):
        if dist(head, tail)>2**0.5:
            hi, hj = head
            ti, tj = tail
            tj += sign(hj-tj)
            ti += sign(hi-ti)
            rope[i] = ti, tj
    visited.add(rope[-1])
print(len(visited))
