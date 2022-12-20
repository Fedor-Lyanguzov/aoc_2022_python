import re
blueprint_re = re.compile(r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')

with open('input') as file:
    bps = [tuple(map(int, blueprint_re.match(x).groups())) for x in file.read().strip().split('\n')]

def quality_level(n, cor, ccl, coob, ccob, corg, cobg):
    def next_minute(m, ore, cla, obs, geo, nor, ncl, nob, nge, bor, bcl, bob, bge):
        nonlocal max_geo
        ore += nor
        cla += ncl
        obs += nob
        geo += nge
        if bor>0:
            bor -= 1
            if bor==0:
                nor += 1
        if bcl>0:
            bcl -= 1
            if bcl==0:
                ncl += 1
        if bob>0:
            bob -= 1
            if bob==0:
                nob += 1
        if bge>0:
            bge -= 1
            if bge==0:
                nge += 1
        if m>=24:
            if max_geo<geo:
                print(geo)
                max_geo=geo
            return
        if bor==bcl==bob==bge==0:
            if ore>=cor:
                next_minute(m+1, ore-cor, cla, obs, geo, nor, ncl, nob, nge, 1, 0, 0, 0)
            if ore>=ccl:
                next_minute(m+1, ore-ccl, cla, obs, geo, nor, ncl, nob, nge, 0, 1, 0, 0)
            if ore>=coob and cla>=ccob:
                next_minute(m+1, ore-coob, cla-ccob, obs, geo, nor, ncl, nob, nge, 0, 0, 1, 0)
            if ore>=corg and obs>=cobg:
                next_minute(m+1, ore-corg, cla, obs-cobg, geo, nor, ncl, nob, nge, 0, 0, 0, 1)
        next_minute(m+1, ore, cla, obs, geo, nor, ncl, nob, nge, bor, bcl, bob, bge)
    max_geo = 0
    next_minute(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0)
    return n*max_geo

print(sum(quality_level(*bp) for bp in bps))


