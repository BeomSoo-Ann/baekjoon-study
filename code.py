# 10815 Number Card

from sys import stdin

N = stdin.readline()
CARD = list(map(str, stdin.readline().split()))


M = stdin.readline()
BASE = list(map(str, stdin.readline().split()))

a = 0


def dfs(list_1):
    global a
    a += 1
    print(a)

    if a >= len(CARD):
        return

    for i in BASE:
        print(i)
        try:
            if i in list_1:

                dfs(list_1[a])
            else:
                dfs(list_1[a])

        except:
            return
    return


dfs(CARD)


print(ANS)
