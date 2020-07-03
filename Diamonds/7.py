'''
4
   D 
  D C
 D C B
D C B A
 D C B
  D C
   D
'''
n = int(input())
for i in range(n):
    print(' '*(n-i-1),end='')
    for j in range(i+1):
        print(chr(64+n-j),end=' ')
    print()

for i in range(n):
    print(' '*(i+1),end='')
    for j in range(n-i-1):
        print(chr(64+n-j),end=' ')
    print()
