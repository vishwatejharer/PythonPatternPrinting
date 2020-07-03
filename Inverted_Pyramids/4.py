'''
5
 1 2 3 4 5
  1 2 3 4
   1 2 3
    1 2
     1
'''
n = int(input())
for i in range(n):
    print(' '*i, end=' ')
    for j in range(n-i):
        print(j+1, end=' ')
    print()
