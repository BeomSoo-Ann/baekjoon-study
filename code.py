# 1436 Movie maker 666


from sys import stdin

N = int(stdin.readline())

def find_Movie():
    BASE = 666
    i = 1
    
    if N == 1:
        return 666
    else:
        while True:
            BASE += 1
            if '666' in str(BASE):
                i += 1
                if i == N:
                    return BASE
                
print(find_Movie())