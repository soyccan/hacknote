from Crypto.Util.number import *

n = 91065253230025247732425967092598538509767353676436114528118074317527802215619882429161904876508240534303234953913943835146683465013713686948500338647558462630226862935445210619962973687178047110032607612332003175654090295771336341765863537626799902913495347392366714183440046838083674733655743831533477606359
c = 74574532840842689947452591462396572547197552613086169808015295349679978115041760768620042225451889845253316059415029322966743472046141305142454642724251869420985365216152662444581608186994935367247716124801197027600472746261823618646644644448403866644213153529598559256639708426453580326523109537744167818540

P.<x> = PolynomialRing(Zmod(n))

for x_len in range(1,126):
    pad = b'\x00' + b'\x87' * (128 - 2 - x_len) + b'\x01'
    pad = bytes_to_long(pad) << (8 * l)

    f = (pad + x) ^ 3 - c

    roots = f.small_roots()
    if roots:
        root = roots[0]
        flag = long_to_bytes(root)
        if flag.startswith(b'FLAG'):
            print(flag)
            break