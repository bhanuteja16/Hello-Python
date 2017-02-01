def fib(a):
	''' Does the fibonacci stuff'''
	b , c = 0, 1
	list = [0]
	while a > 1:
		list.append(c)
		b , c = c , b + c
		a -= 1
	return(list)
	
num = int(input("Enter the number of fibonacci number you want: "))
print(fib.__doc__)
print(fib(num))