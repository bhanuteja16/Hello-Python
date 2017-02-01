num1 = int(input("Enter a Number " ))

num2 = (num1 // 2) + 1

list = range(2
, num2)
div = []

for x in list:
	if num1 % x == 0:
		div.append(x)

print("List of Divisors: " + str(div))

