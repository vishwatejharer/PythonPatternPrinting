'''
E
E D
E D C
E D C B
E D C B A
E D C B
E D C
E D
E
'''
n = int(input())

for i in range(n):
    for j in range(i+1):
        print(chr(64+n-j), end=' ')
    print()

for i in range(n-1):
    for j in range(n-i-1):
        print(chr(64+n-j), end=' ')
    print()