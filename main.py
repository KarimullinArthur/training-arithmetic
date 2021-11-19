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

		if result != c:
			print(Fore.RED + 'Wrong',Style.RESET_ALL, a,mode,b,"=",c)

def difficulty(d):
	
	if d == "easy":
		return 10 
	if d == "norm":
		return 1000
	if d == "hard":
		return 10000

def menu():	
	print("Hello")
	while True==True:
		print("+ |sum","- |subtraction",sep='\n')
		
		mode = input()
		if mode == "exit" or mode == "":
			break
		
		print("1-100 |easy","100-1000 |norm","1000-10000 |hard",sep='\n')
		
		diff = input()
		
		if mode == "+":
			main("+",difficulty(diff)/10,difficulty(diff)*10)
		if mode == "-":
			main("-",difficulty(diff)/10,difficulty(diff)*10)
	
		else:
			print("Ops,something wrong")

		
menu()
