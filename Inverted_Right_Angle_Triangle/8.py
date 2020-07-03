'''
6
F E D C B A
F E D C B
F E D C
F E D
F E
F
'''
n = int(input())
for i in range(n):
    for j in range(n-i):
        print(chr(64+n-j), end=' ')
    print()
