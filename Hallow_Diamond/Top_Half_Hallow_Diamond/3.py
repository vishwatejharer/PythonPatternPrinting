'''
5
        A
      B   B
    C       C
  D           D
E               E
'''
n = int(input())

for i in range(n):
    print('  ' * (n - i - 1) + chr(65 + i) + ' ', end='')
    if i >= 1:
        print('  ' * (2 * i - 1) + chr(65 + i), end='')
    print()
