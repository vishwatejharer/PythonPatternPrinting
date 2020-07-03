'''
1               1
  2           2
    3       3
      4   4
        5
'''
n = int(input())

for i in range(n):
    print('  ' * i + str(i + 1) + ' ', end='')
    if i != (n - 1):
        print('  ' * (2 * n - 2 * i - 3) + str(i + 1), end='')
    print()
