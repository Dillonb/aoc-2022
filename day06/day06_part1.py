#!/usr/bin/env python3
print([i + 4 for i, n in [list(zip(range(0, len(l)-4), [len(set(l[i:i+4])) for i in range(0, len(l)-4)])) for l in [open("input").read().strip()]][0] if n == 4][0])