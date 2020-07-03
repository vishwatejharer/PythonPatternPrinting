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

# Top Part: n rows
for i in range(n):
    print('* '*(i+1))

# Bottom Part: n-1 rows
for i in range(n-1):
    print('* '*(n-i-1))
