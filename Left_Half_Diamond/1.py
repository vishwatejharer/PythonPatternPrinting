'''
4
      *
    * *
  * * *
* * * *
  * * *
    * *
      *
'''
n = int(input())
# First half" n rows
for i in range(n):
    print('  '*(n-i-1) + '* '*(i+1)) # '  ' => Two Spaces

# Second Half: n-1 rows
for i in range(n-1):
    print('  '*(i+1) + '* '*(n-i-1))
