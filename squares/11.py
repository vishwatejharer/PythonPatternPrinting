'''
4
D C B A
D C B A
D C B A
D C B A 
'''
n = int(input())
for i in range(n):
    for j in range(n):
        print((chr(64 + n - j)),end=' ')
    print()