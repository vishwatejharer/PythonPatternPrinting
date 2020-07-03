'''
* * * * *
    *
    *
    *
    *
    *
* * * * *
'''
for row in range(7):
    for col in range(5):
        if row in {0, 6}:
            print('*', end=' ')
        elif (row in range(1, 6)) and col == 2:
            print('*', end=' ')
        else:
            print(' ', end= ' ')
    print()