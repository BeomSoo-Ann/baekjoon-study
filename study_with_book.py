import time
import sys

N, M, K = map(int, sys.stdin.readline().split())
DATA = list(map(int, sys.stdin.readline().split()))

DATA.sort()

result = 0
cnt = 0

start_time = time.time()

while True:
    try:
        if cnt == K:
            result += DATA[N-2]
            M -= 1
            cnt = 0

            if M == 0:
                break

            continue

        result += DATA[N-1]
        M -= 1
        cnt += 1

        if M == 0:
            break

    except:
        break

print(result)


end_time = time.time()
print("time :", end_time - start_time)


# not just code, make algorithm


start_time2 = time.time()

count = M / (K + 1) * K + M % (K + 1)

result += count * DATA[N-1]
result += (M - count) * DATA[N-2]

print(result)

end_time2 = time.time()
print("time :", end_time2 - start_time2)
