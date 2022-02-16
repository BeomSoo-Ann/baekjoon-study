# No.9184

from sys import stdin, stdout



def w(a, b, c):
    if a <=0 or b <= 0 or c <= 0:
        return 1
    
    elif a > 20 or b > 20 or c > 20:
        return 1048576
    
    elif a == b == c:
        return 2**a
    
    elif b > c:
        return w(a, c, b)
    
    elif a < b and b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    
    elif a == 1:
        return 2
    
    else:
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)


while True:
    A, B, C = map(int, stdin.readline().split())
    if A == B == C == -1:
        break
    
    print(w(A, B, C))
    
    