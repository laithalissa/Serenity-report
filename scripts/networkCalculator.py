

S_VALUES = [15, 30, 45, 60]
N_VALUES = [2,  4,  8,  16]

def f(s, n): return s * n * 60.4

for s in S_VALUES:
    for n in N_VALUES:
	print "(s: %s, n: %s) = %1.2f kB" % (s, n, f(s, n)/1024.0)


