list = [3,6,76,93,45,26,78,4,9,73,52,14,19,63,84,98,26,43,44]

num = int(input("Enter a Number "))

num1 = []

for ex in list:
	if ex < num :
		num1.append(ex)

print(num1)

