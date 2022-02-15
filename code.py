# No.14889 team battle

from sys import stdin


N = int(stdin.readline())
teamstate_list = [list(map(int, stdin.readline().split())) for _ in range(N)]
L = []
mem_list = []
start_score = []
link_score = []


def check_score(L):
    score = 0
    for i in range(len(L)-1):
        for j in range(i+1, len(L)):
            score += teamstate_list[L[i]][L[j]] + teamstate_list[L[j]][L[i]]
    return score


def backtrace_start():
    if len(L) == N//2:
        start_score.append(check_score(L))
        return

    for i in range(N):
        if i in L:
            continue

        if len(L) == 1:
            if L[0] != 0:
                continue

        L.append(i)

        if len(L) != 1:
            if L[-1] < L[-2]:
                L.pop()
                continue
        backtrace_start()
        L.pop()


def backtrace_link():
    if len(L) == N//2:
        link_score.append(check_score(L))
        return

    for i in range(N):
        if i in L:
            continue

        if len(L) == 1:
            if L[0] == 0:
                continue

        L.append(i)

        if len(L) != 1:
            if L[-1] < L[-2]:
                L.pop()
                continue
        backtrace_link()
        L.pop()


backtrace_start()
backtrace_link()
link_score.reverse()

sub_list = []
for i in range(len(link_score)):
    sub_list.append(abs(link_score[i] - start_score[i]))

print(min(sub_list))
