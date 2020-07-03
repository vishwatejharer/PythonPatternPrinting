'''
5
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''
n = int(input())
# First Half
for i in range(n):
    print(' '*(n-i-1) + '* '*(i+1))
# Second Half, n-1 rows
for i in range(n-1):
    print(' '*(i+1) + '* '*(n-i-1))
