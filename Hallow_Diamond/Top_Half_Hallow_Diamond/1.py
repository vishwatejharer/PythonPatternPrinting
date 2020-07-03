'''
5
        *
      *   *
    *       *
  *           *
*               *
'''
n = int(input())

for i in range(n):
    print('  ' * (n - i - 1) + '* ', end='')  # Two spaces
    if i >= 1:  # From Second row onwards
        print('  ' * (2 * i - 1) + '*', end='')
    print()
