'''
E               E
  D           D
    C       C
      B   B
        A
'''
n = int(input())

for i in range(n):
    print('  ' * i + chr(64 + n - i) + ' ', end='')
    if i != (n - 1):
        print('  ' * (2 * n - 2 * i - 3) + chr(64 + n - i), end='')
    print()
