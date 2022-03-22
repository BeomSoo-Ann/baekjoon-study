# No.11054 longest "bytonic" increasing sequence


from sys import stdin


N = int(stdin.readline())
wire = [list(map(int, stdin.readline().split())) for _ in range(N)]
L = []


def check_wire():
    for i in range(N):
        if len(L) == 0:
            L.append(wire[i])
            check_wire()
            L.pop()

        elif len(L) != 0:
            if wire[i] in L:
                continue

            if L[-1][0] < wire[i][0] and L[-1][1] < wire[i][1]:
                L.append(wire[i])
                check_wire()
                L.pop()


check_wire()
