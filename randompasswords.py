#This imports the random module generates random numbers and selecting random elements.
import random

uppercase_letters = "ABCDEFGHIJKLMOPQRSTUVWXYZ"

lowercase_letters = uppercase_letters.lower()

digits = "0123456789"

symbols = "@$%?*&^!+=><~"
#These variables store the different character sets: uppercase letters, lowercase letters, digits, and symbols.
upper, lower, nums, syms = True, True, True, True
#These Boolean variables determine which character sets will be included in the password generation. If True, the corresponding character set will be used, if you make them false that, wont be in the password.
all = ""

if upper:
	all += uppercase_letters
if lower:
	all += lowercase_letters
if nums: 
	all += digits
if syms:
	all += symbols

#The character sets are concatenated into a single string called all based on the inclusion flags. This string will be used to generate the password.
length = 25

amount = 15
#The length variable defines the length of each password, and the amount variable determines the number of passwords to generate.
for x in range(amount):
	password = "".join(random.sample(all,length))
	print(password)
#In this loop, random.sample() is used to select a random sample of characters from the all string of the specified length. The characters are then joined together to form a password. This process is repeated amount times, and each password is printed.
#This code shows the breakdown of how password generates random passwords based on the specified character sets and inclusion flags.