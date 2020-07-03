'''
5
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
'''
n = int(input())
for i in range(n):
    for j in range(n):
        print(n-j,end=' ')
        #print((str(n-j)),end=' ')
    print()