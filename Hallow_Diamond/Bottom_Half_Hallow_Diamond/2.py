'''
5               5
  4           4
    3       3
      2   2
        1
'''
n = int(input())

for i in range(n):
    print('  ' * i + str(n - i) + ' ', end='')
    if i != (n - 1):
        print('  ' * (2 * n - 2 * i - 3) + str(n - i), end='')
    print()