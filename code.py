# No.1181

from sys import stdin, stdout

N = int(stdin.readline())
word_list = []

for _ in range(N):
    word = stdin.readline().strip()
    
    if word not in word_list:
        word_list.append(word)
        
sorted_list = sorted(word_list, key = lambda x: (len(x), x))

for word in sorted_list:
    stdout.write(word + '\n')