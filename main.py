import random
from colorama import Fore, Style
import operator

ops = { "+": operator.add, "-": operator.sub }

def main(mode,x=1,y=100):
	while True==True:
		a = random.randint(x,y)
		b = random.randint(x,y)
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
	while True==True:
		print("+ |sum","- |subtraction",sep='\n')
		
		mode = input()
		
		if mode == "+":
			main("+")
		if mode == "-":
			main("-")
		if mode == "exit":
			break	
		else:
			print("Ops,something wrong")

		
menu()
