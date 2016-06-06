import random

game = "True"

while game == "True":
	num2 = random.randint(1,10)
	print("Random Number Generated")
	count = 1
	while True:
		num1 = int(input("Guess a number that is generated between 1 and 9 \n"))
		if num2 - num1 > 0:
			print("You have guessed too low")
		elif num2 - num1 < 0:
			print("you have guessed too High")
		else:
			print("Hurray you guessed it correct, and it took you ",count," attempts")
			break
		count += 1
	cont = input("Press 'c' to continue or any other key to exit \n")
	if cont == 'c':
		continue
	else:
		break
