'''
5
1 1 1 1 1
 2 2 2 2
  3 3 3
   4 4
    5

'''
n = int(input())
for i in range(n):
    print(' '*i + (str(i+1)+' ')*(n-i))
