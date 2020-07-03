n = int(input())
# Top half : n rows
for i in range(n):
    print('  ' * (n - i - 1) + '* ', end='')
    if i != 0:
        print('  ' * (2 * i - 1) + '*', end='')
    print()

# Bottom Half : n-1 rows : 2n-2i-5 spaces
for i in range(n-1):
    print('  ' * (i+1) + '* ', end='')
    if i != n-2: #Except last row in bottom half
        print('  ' * (2 * n - 2 * i - 5) + '*', end='')
    print()
