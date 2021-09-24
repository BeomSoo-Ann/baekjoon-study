# 1193 분수찾기
# 1 -> 1, 2 -> 3, 2, 1 -> 1, 2, 3, 4 -> 5, 4, 3, 2, 1

X = int(input())
n = 1


def finder(n, X):
    a = []
    for num in range(n):
        a.append(num+1)

    if n % 2 == 0:
        print(str(a[X-1])+'/'+str(a[n-X]))

    elif n % 2 != 0:
        print(str(a[n-X])+'/'+str(a[X-1]))

    else:
        pass


while True:
    try:
        X -= n
        n += 1
        if X == 0:
            print('1/1')
        elif X <= n:
            finder(n, X)
            break
        else:
            pass

    except:
        break
