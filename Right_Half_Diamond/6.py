'''
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''
n = int(input())

for i in range(n):
    for j in range(i+1):
        print(n-j, end=' ')
    print()

for i in range(n-1):
    for j in range(n-i-1):
        print(n-j, end=' ')
    print()
