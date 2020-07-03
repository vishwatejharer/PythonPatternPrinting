'''
* * * * *
    *
    *
    *
    *
    *
    *
'''
for row in range(7):
    for col in range(5):
        if row == 0:
            print('*', end=' ')
        elif row in range(1,7) and col == 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()