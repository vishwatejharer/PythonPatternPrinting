'''
5
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''
n = int(input())
for i in range(n):
    for j in range(n-i):
        print(n-j, end=' ')
    print()
