#!/usr/bin/env python3
initial,steps = open("input").read().split("\n\n")
initial = initial.split("\n")[:-1]

state = [[] for _ in range(((len(initial[-1])//4)+1))]

for l in reversed(initial):
    for s,i in enumerate(range(1, len(initial[-1]), 4)):
        b = l[i]
        if b != ' ':
            state[s].append(b)

for step in steps.split("\n"):
    _,n,_,f,_,t = step.split(" ")
    for _ in range(0, int(n)):
        state[int(t)-1].append(state[int(f)-1].pop())

print("".join([x[-1] for x in state]))
