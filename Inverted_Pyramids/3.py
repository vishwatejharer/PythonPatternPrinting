'''
5
A A A A A
 B B B B
  C C C
   D D
    E

'''
n = int(input())
for i in range(n):
    print(' '*i + (chr(65+i)+' ')*(n-i))
