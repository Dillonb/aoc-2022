#!/usr/bin/env python3
print([i + 14 for i, n in [list(zip(range(0, len(l)-14), [len(set(l[i:i+14])) for i in range(0, len(l)-14)])) for l in [open("input").read().strip()]][0] if n == 14][0])