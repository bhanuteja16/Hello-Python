from datetime import date



name = input("Give me your name: ")
print("Your Name is " + name)
age = input("Enter your age: ")
#print(type(age), id(age), age)
age = int(age)
#print(type(age), id(age), age)
today = str(date.today())
#print(today)
year = int(today[0:4])
#print(type(year), year)
y=str(year + (100-age))
print(name +  " will be Hunderd years by " + y)
