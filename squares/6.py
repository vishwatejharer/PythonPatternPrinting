'''
1  2  3  4  5
1  2  3  4  5
1  2  3  4  5
1  2  3  4  5
1  2  3  4  5
'''
n = int(input())
for i in range(n):
    # Every character is changing in a row; so take 2 for loops
    for j in range(n):
        print(str(j+1),end=' ') #end= ' ' : gives an extra space after character it also acts as end char
        #print(j + 1, end=' ')
    print()
