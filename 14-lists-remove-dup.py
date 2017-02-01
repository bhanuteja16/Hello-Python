def no_duplic(list1):
	list2 = set(list1)
	return(list2)
	
	
ls = list(input("Enter the list  \n "))
print(no_duplic(ls))