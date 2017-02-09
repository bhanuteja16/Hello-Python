#! /bin/python3

def check_rows(lst) :
    fun = False
    for ls in lst :
        if(all(x == ls[0] for x in ls)) :
            fun = True
            return (fun, ls[0])

def check_col(lst) :
    for i in range(3) :
        ls = []
        for j in range(3) :
            ls.append(lst[i][j])
        if(all(x == ls[0] for x in ls)) :
            return (True, ls[0])
    pass

def check_dia(lst) :
    pass


lst1 = list(input("Enter the first row elements: "))
lst2 = list(input("Enter the second row elements: "))
lst3 = list(input("Enter the third row elements: "))
lst = [lst1, lst2, lst3]
a, b = check_rows(lst)
print (a, b)


