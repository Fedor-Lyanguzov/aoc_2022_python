

with open("input.py") as file:
    f = file.read().split('\n')[10:-1]
d = {
    1: "HTZD",
    2: "QRWTGCS",
    3: "PBFQNRCH",
    4: "LCNFHZ",
    5: "GLFQS",
    6: "VPWZBRCS",
    7: "ZFJ",
    8: "DLVZRHQ",
    9: "BHGNFZLD",
    }
def make_command(x):
    x = x.split()
    x = x[1], x[3], x[5]
    return tuple(map(int, x))
cmds = list(map(make_command, f))

def process(d, cmds):
    d = {k: list(v) for k, v in d.items()}
    for n, i, j in cmds:
        for _ in range(n):
            d[j].append(d[i].pop())
    return "".join(d[i][-1] for i in range(1, 10))
print(process(d, cmds))

def process2(d, cmds):
    d = {k: list(v) for k, v in d.items()}
    for n, i, j in cmds:
        d[j].extend(d[i][-n:])
        del d[i][-n:]
    return "".join(d[i][-1] for i in range(1, 10))
print(process2(d, cmds))
