'''
5
E E E E E
D D D D D
C C C C C
B B B B B
A A A A A
'''
n = int(input())
for i in range(n):
    print((chr(64 + n - i) + ' ') * n) # Start from 64 , not 65 -> A
