'''
5
        E
      D   D
    C       C
  B           B
A               A

'''
n = int(input())

for i in range(n):
    print('  ' * (n - i - 1) + chr(64 + n - i) + ' ', end='')
    if i >= 1:
        print('  ' * (2 * i - 1) + chr(64 + n - i), end='')
    print()
