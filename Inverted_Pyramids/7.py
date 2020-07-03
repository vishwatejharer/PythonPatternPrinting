'''
5
E D C B A
 E D C B
  E D C
   E D
    E
'''
n = int(input())
for i in range(n):
    print(' '*i, end='')
    for j in range(n-i):
        print(chr(64+n-j), end=' ')
    print()
