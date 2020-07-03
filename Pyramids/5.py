'''
5
     E
    E D
   E D C
  E D C B
 E D C B A
'''
n = int(input())
for i in range(n):
    print(' '*(n-i-1), end=' ')
    for j in range(i+1):
        print(chr(64+n-j), end=' ')
    print()
