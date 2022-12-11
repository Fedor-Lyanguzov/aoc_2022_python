from math import prod

def make_monkeys():
    monkeys = {
            0: [
                [63, 84, 80, 83, 84, 53, 88, 72],
                lambda x: x*11,
                lambda x: x%13==0,
                4, 7],
            1: [
                [67, 56, 92, 88, 84],
                lambda x: x+4,
                lambda x: x%11==0,
                5, 3],
            2: [
                [52],
                lambda x: x*x,
                lambda x: x%2==0,
                3, 1],
            3: [
                [59, 53, 60, 92, 69, 72],
                lambda x: x+2,
                lambda x: x%5==0,
                5, 6],
            4: [
                [61, 52, 55, 61],
                lambda x: x+3,
                lambda x: x%7==0,
                7, 2],
            5: [
                [79, 53],
                lambda x: x+1,
                lambda x: x%3==0,
                0, 6],
            6: [
                [59, 86, 67, 95, 92, 77, 91],
                lambda x: x+5,
                lambda x: x%19==0,
                4, 0],
            7: [
                [58, 83, 89],
                lambda x: x*19,
                lambda x: x%17==0,
                2, 1],
            }
    return monkeys

def reduce_worry(item):
    return item//3

def turn(monkey, i, monkey_business, reduce_worry=lambda x: x):
    items, inspect, test, left, right = monkey
    while items:
        item = items.pop(0)
        item = inspect(item)
        monkey_business[i] += 1
        item = reduce_worry(item)
        if test(item):
            monkeys[left][0].append(item)
        else:
            monkeys[right][0].append(item)

def make_turns(n, reduce_worry=lambda x: x):
    global monkeys
    monkeys = make_monkeys()
    monkey_business = {i:0 for i in range(8)}
    for _ in range(n):
        for i in range(8):
            turn(monkeys[i], i, monkey_business, reduce_worry)
    return prod(sorted(monkey_business.values())[-2:])

print(make_turns(20, reduce_worry))

mods = [13, 11, 2, 5, 7, 3, 19, 17]
M = prod(mods)

print(make_turns(10_000, lambda x: x%M))
