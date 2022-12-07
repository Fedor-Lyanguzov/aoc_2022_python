
with open("input") as file:
    log = file.read().strip().split('\n')


def make_dir(name, parent):
    if name.startswith('dir '):
        name = name[4:]
    return [name, parent, [], [], 0]

root = make_dir('/', None)
current = root
log = iter(log)
next(log)
line = next(log, None)
while line is not None:
    if line=="$ cd ..":
        current = current[1]
        line = next(log, None)
        continue
    elif line.startswith("$ cd "):
        d = line[5:]
        for dir in current[2]:
            if dir[0]==d:
                current = dir
                break
        else:
            print('did not cd')
        line = next(log, None)
        continue
    elif line=="$ ls":
        line = next(log, None)
        while not (line is None or line.startswith("$")):
            if line.startswith('dir '):
                current[2].append(make_dir(line, current))
            else:
                size, name = line.split()
                size = int(size)
                current[3].append((size, name))
            line = next(log, None)

def size(tree):
    files = sum(x[0] for x in tree[3])
    dirs = sum(size(x) for x in tree[2])
    tree[4] = files+dirs
    return files+dirs

size(root)
def all_dirs(tree):
    yield tree
    for x in tree[2]:
        yield from all_dirs(x)
print(sum(map(lambda x: x[4], filter(lambda x: x[4]<=100_000, all_dirs(root)))))
print(min(map(lambda x: x[4], filter(lambda x: 70_000_000-root[4]+x[4]>=30_000_000, all_dirs(root)))))


