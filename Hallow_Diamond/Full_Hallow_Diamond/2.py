'''
       1
      2   2
    3       3
  4           4
5               5
  4           4
    3       3
      2   2
        1

'''
n = int(input())

for i in range(n):
    print('  '* (n - i - 1) + str(i + 1) + ' ', end='')
    if i != 0:
        print('  ' * (2 * i - 1) + str(i + 1), end='')
    print()

for i in range(n-1):
    print('  ' * (i + 1) + str(n - i - 1) + ' ', end='')
    if i != n-2:
        print('  ' * (2 * n - 2 * i - 5) + str(n - i - 1), end='')
    print()
