import math

def Primecheck(a):
	b = int(math.sqrt(a)) + 1 
	while b > 1: 
		if a % b == 0:
			print(" It is not a prime number")
			b = 0
			break
		b -= 1	
	if b != 0:
		print("Its is a prime number")
		
	
num = int(input("Enter the number: "))
Primecheck(num)
