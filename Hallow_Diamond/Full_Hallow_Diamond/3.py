'''
        E
      D   D
    C       C
  B           B
A               A
  B           B
    C       C
      D   D
        E
'''
n = int(input())

for i in range(n):
    print('  '* (n - i - 1) + chr(64 + n - i) + ' ', end='')
    if i != 0:
        print('  ' * (2 * i - 1) + chr(64 + n - i), end='')
    print()

for i in range(n-1):
    print('  ' * (i + 1) + chr(66 + i) + ' ', end='')
    if i != n-2:
        print('  ' * (2 * n - 2 * i - 5) + chr(66 + i), end='')
    print()