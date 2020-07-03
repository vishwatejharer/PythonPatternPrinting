'''
        5
      4   4
    3       3
  2           2
1               1
  2           2
    3       3
      4   4
        5
'''
n = int(input())

for i in range(n):
    print('  '* (n - i - 1) + str(n - i) + ' ', end='')
    if i != 0:
        print('  ' * (2 * i - 1) + str(n - i), end='')
    print()

for i in range(n-1):
    print('  ' * (i + 1) + str(i + 2) + ' ', end='')
    if i != n-2:
        print('  ' * (2 * n - 2 * i - 5) + str(i + 2), end='')
    print()