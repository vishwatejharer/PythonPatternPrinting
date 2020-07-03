'''
6
A A A A A A
B B B B B
C C C C
D D D
E E
F
'''
n = int(input())
for i in range(n):
    print((chr(65+i)+' ')*(n-i))