'''
* * * * *
*
*
* * * * *
*
*
* * * * *
'''
for row in range(7):
    for col in range(5):
        if row % 3 == 0:
            print('*', end=' ')
        elif (row % 3 != 0) and col == 0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()