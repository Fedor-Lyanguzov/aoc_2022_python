
with open('input') as file:
    cmds = file.read().strip().split('\n')

def execute(cmds):
    x = 1
    for cmd in cmds:
        if cmd=='noop':
            yield x
        elif cmd.startswith('addx '):
            _, v = cmd.split()
            v = int(v)
            yield x
            yield x
            x += v

def f(x):
    return ((res, i) for res, i in zip(execute(cmds), range(1, x+1)) if i in range(20, 260, 40))


print(sum(res*i for res, i in f(220)))

x = iter(execute(cmds))
for i in range(6):
    for j in range(40):
        r = next(x)
        if r-1<=j<=r+1:
            c = "#"
        else:
            c = '.'
        print(c, end='')
    print()
