number = int(input("Input any number: ") )
k = number % 4
j = number % 2

if ( k == 0):
	print("Number is divisible by 4 and is even")

else:
	if ( j == 1):
		print("Number is odd")

	else :
		print("Number is even")


num1 = int(input("Input your first number: "))
num2 = int(input("Input your second number: "))

if (num1 % num2 == 0):
	print(str(num1) + " is divisible by " + str(num2))

else:
	print(str(num1) + " is not divisible by " + str(num2))
