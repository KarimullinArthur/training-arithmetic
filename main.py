import random
from colorama import Fore, Style
import operator

ops = { "+": operator.add, "-": operator.sub }


def main(mode):
	while True==True:
		a = random.randint(1,100)
		b = random.randint(1,100)
		c = ops[mode](a,b)

		print(a,mode,b,"= ", end='')
		result = input()

		if result == "exit":
			break

		result = int(result)

		if result == c:
			print(Fore.GREEN + 'Right',Style.RESET_ALL)

		else :
			print(Fore.RED + 'Wrong',Style.RESET_ALL, a,mode,b,"=",c)


def menu():
	print("Hello")
	print("+ |sum","- |subtraction",sep='\n')
	
	mode = input()
	
	if mode == "+":
		main("+")
	if mode == "-":
		main("-")
	
	
menu()

