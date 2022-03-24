# No.11054 longest "bytonic" increasing sequence


from sys import stdin

from aem import con


N = int(stdin.readline())
wire = [list(map(int, stdin.readline().split())) for _ in range(N)]
L = []
print(wire)

base = wire


def check_wire():
    for line in wire:
        for i in wire:
            if line == i:
                continue

            if line[0] < i[0] and line[1] > i[1]:
                print(i)
            elif line[0] > i[0] and line[1] < i[1]:
                print(i)
            else:
                continue


check_wire()
