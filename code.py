# No.1912

from sys import stdin


N, K = map(int, stdin.readline().split())
baggage = [list(map(int, stdin.readline().split())) for _ in range(N)]
# 무게 순으로 정렬함
baggage.sort(key=lambda x: x[0])
L = []
total_weight = 0


print(baggage)

# 무게 순으로 정렬 후에
# Max Weight - First item weight를 해서 남은 무게를 저장
# 남은 무게보다 물품 무게가 크면 스킵


def dfs():
    global total_weight

    if total_weight > K:
        return

    for i in range(N):
        if baggage[i] in L:
            continue

        L.append(baggage[i])

        if len(L) != 1:
            if baggage.index(L[-2]) > baggage.index(L[-1]):
                L.pop()
                continue

        total_weight = sum([item[0] for item in L])
        dfs()
        L.pop()
