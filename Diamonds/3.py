'''
4
   A
  B B
 C C C
D D D D
 C C C
  B B
   A
'''
n = int(input())
for i in range(n):
    print(' '*(n-i-1) + (chr(65+i)+' ')*(i+1))
for i in range(n-1):
    print(' '*(i+1) + (chr(64+n-i-1)+' ')*(n-i-1))
