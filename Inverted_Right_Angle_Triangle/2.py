'''
6
1 1 1 1 1 1
2 2 2 2 2
3 3 3 3
4 4 4
5 5
6
'''
n = int(input())
for i in range(n):
    print((str(i+1)+' ')*(n-i))