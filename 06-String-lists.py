str = input ("Enter the string: ")
a = len(str)  
str1 = str[::-1]

if str == str1:
	print("String is palindrome")
else:
	print("String is not palindrome")
