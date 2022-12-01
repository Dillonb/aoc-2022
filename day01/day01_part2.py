#!/usr/bin/env python3
print(sum(sorted([sum([int(f) for f in elf.strip().split("\n")]) for elf in open("input").read().split("\n\n")], reverse=True)[:3]))