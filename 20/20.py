from dataclasses import dataclass

with open('input') as file:
    xs = [int(x) for x in file.read().strip().split('\n')]

@dataclass
class Node:
    p: 'Node'
    n: 'Node'
    d: int
    def __str__(self):
        return str(self.d)
    __repr__ = __str__
    def move(self, i):
        if i==0:
            return
        if i>0:
            left1 = self.p
            left2 = self.n
            left1.n = left2
            left2.p = left1
            right1 = self
            for _ in range(i%(len(xs)-1)):
                right1 = right1.n
            right2 = right1.n
            right1.n = self
            right2.p = self
            self.p = right1
            self.n = right2
        else:
            right1 = self.p
            right2 = self.n
            right1.n = right2
            right2.p = right1
            left2 = self
            for _ in range((-i)%(len(xs)-1)):
                left2 = left2.p
            left1 = left2.p
            left1.n = self
            left2.p = self
            self.p = left1
            self.n = left2


nodes = [Node(None, None, x) for x in xs]
for l, r in zip(nodes, nodes[1:]):
    l.n = r
    r.p = l
nodes[0].p = nodes[-1]
nodes[-1].n = nodes[0]
for x in nodes:
    x.move(x.d)
s = 0
zero = nodes[xs.index(0)]
for _ in range(3):
    for _ in range(1000):
        zero = zero.n
    s += zero.d
print(s)

nodes = [Node(None, None, x*811589153) for x in xs]
for l, r in zip(nodes, nodes[1:]):
    l.n = r
    r.p = l
nodes[0].p = nodes[-1]
nodes[-1].n = nodes[0]
for _ in range(10):
    for x in nodes:
        x.move(x.d)
s = 0
zero = nodes[xs.index(0)]
for _ in range(3):
    for _ in range(1000):
        zero = zero.n
    s += zero.d
print(s)
