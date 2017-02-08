#! /bin/python3

def grid(row,col):
    rowlst = [' -- ' * col]
    col = col + 1
    collst = ['|   ' * col]
    for r in range(row) :
        print (' '.join(rowlst))
        print ('  '.join(collst))
    print (' '.join(rowlst))

row = int(input("Enter number of rows: "))
col = int(input("Enter number of col: "))
grid(row,col)
