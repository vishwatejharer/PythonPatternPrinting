'''
* * * * *
    *
    *
    *
    *
*   *
  *
'''
for row in range(7):
    for col in range(5):
        if row == 0 :
            print('*', end=' ')
        elif row in range(1,6) and col == 2:
            print('*', end=' ')
        elif (row == 5 and col == 0) or (row == 6 and col == 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()