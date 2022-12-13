
with open('input') as file:
    packets = list(tuple(map(eval, x.split('\n'))) for x in file.read().strip().split('\n\n'))


def is_int(x):
    return isinstance(x, int)
def is_list(x):
    return isinstance(x, list)

def compare_packets(l, r):
    def compare(left, right):
        nonlocal result, done
        if not done:
            if is_int(left) and is_int(right):
                if left>right:
                    result = False
                    done = True
                elif left<right:
                    result = True
                    done = True
            elif is_list(left) and is_list(right):
                for l, r in zip(left, right):
                    compare(l, r)
                    if done:
                        break
                else:
                    if len(right)<len(left):
                        result = False
                        done = True
                    elif len(left)<len(right):
                        result = True
                        done = True
            elif is_int(left):
                compare([left], right)
            else:
                compare(left, [right])
    result = None
    done = False
    compare(l, r)
    return result

print(sum(i for i, (l, r) in enumerate(packets, 1) if compare_packets(l, r)))
packets = [x for y in packets for x in y] + [[[2]], [[6]]]

for i in range(len(packets)):
    for j in range(len(packets)-1):
        if not compare_packets(packets[j], packets[j+1]):
            packets[j], packets[j+1] = packets[j+1], packets[j]
a = -1
b = -1
for i in range(len(packets)):
    if packets[i]==[[2]]:
        a = i+1
    if packets[i]==[[6]]:
        b = i+1
print(a*b)


