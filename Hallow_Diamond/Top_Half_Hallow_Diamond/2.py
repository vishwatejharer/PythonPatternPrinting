'''
5
        1
      2   2
    3       3
  4           4
5               5
'''
n = int(input())

for i in range(n):
    print('  ' * (n - i - 1) + str(i + 1) + ' ', end='')
    if i >= 1:
        print('  ' * (2 * i - 1) + str(i + 1), end='')
    print()