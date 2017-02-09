#! /bin/python3

print ("Guess a number between 0 and 100")
lst = list(range(0,101))
guess = 0
while True :
    guess = guess + 1
    mid = len(lst) // 2
    print ("Is the number: {}. If you guessed number is greater then {} then press G, if the gussed number is smaller than {} then press S finally if the number is equal to {} press E".format(lst[mid], lst[mid], lst[mid], lst[mid]))
    choice = str(input())
    if choice == "E" or choice == "e" :
        print ("Finally gussed it")
        print ("It took {} guesses".format(guess))
        break
    elif choice == "G" or choice == "g" :
        lst = lst[mid + 1:len(lst)]
    elif choice == "S" or choice == "s" :
        lst = lst[0:mid]
    else :
        print ("Invalid choice, exiting ...")
        exit()
