'''
*       *
*       *
* *     *
*   *   *
*     * *
*       *
*       *
'''
for row in range(7):
    for col in range(5):
        if col in (0,4):
            print('*',end=' ')
        elif (row == 2 and col == 1) or (row == 3 and col == 2) or (row == 4 and col == 3):
            print('*', end=' ')

        else:
            print(' ', end=' ')
    print()