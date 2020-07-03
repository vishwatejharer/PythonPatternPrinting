'''
F F F F F F
E E E E E
D D D D
C C C
B B
A
'''
n = int(input())
for i in range(n):
    print((chr(64+n-i)+' ')*(n-i))