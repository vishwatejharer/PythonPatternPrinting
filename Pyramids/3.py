'''
5
    A
   B B
  C C C
 D D D D
E E E E E
'''
n = int(input())
for i in range(n):
    print(' '*(n-i-1) + (chr(65+i)+' ')*(i+1))