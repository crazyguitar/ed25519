t = [2**(64*t) for t in range(10)]
p = 2**255 - 19

def field(e):
    acc = 0
    for i in range(len(e)):
        acc += e[i]*t[i]
    return acc

x = field([140194305, 1, 2955487002624, 1, 2955487002624])
y = field([16384, 16384, 16384, 16384, 2955487002624])

z = field([2296943493120,2296943509504,48424995994501120,48424995994517504,8610922045896736768,96848353589002262,1217319147952685056,48425654538467760,1168896448901677056,473520])

print((x*y) % p == z % p)