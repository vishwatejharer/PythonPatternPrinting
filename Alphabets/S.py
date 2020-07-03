'''
  * * * *
*
*
* * * *
        *
        *
* * * *
'''
for row in range(7):
    for col in range(5):
        if row == 0 and col != 0:
            print('*', end= ' ')
        elif row in {3, 6} and col != 4:
            print('*', end=' ')
        elif row in {1, 2} and col == 0:
            print('*', end=' ')
        elif row in {4,5} and col == 4:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


