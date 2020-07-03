'''
5
        5
      4   4
    3       3
  2           2
1               1

'''
n = int(input())

for i in range(n):
    print('  ' * (n - i - 1) + str(n - i) + ' ', end='')
    if i >= 1:
        print('  ' * (2 * i - 1) + str(n - i), end='')
    print()
