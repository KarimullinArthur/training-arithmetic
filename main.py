import random
from colorama import Fore, Style
import operator

ops = { '+': operator.add, '-': operator.sub } # '+' = + ; '-' = -o

def main(mode,x=1,y=100):
			while True:
				a = random.randint(x,y)
				b = random.randint(x,y)
				c = ops[mode](a,b)

				print(a,mode,b,"= ", end='')
				try:
					result = input()
					if result == 'exit' or result == '':
						break
				except ValueError:
					print("Ops,something wrong")
				result = int(result)

				if result == c:
					print(Fore.GREEN + 'Right',Style.RESET_ALL)

				if result != c:
					print(Fore.RED + 'Wrong',Style.RESET_ALL, a,mode,b,"=",c)

#def exit(i):
#	if mode == "exit" or mode == "":
#		break
def difficulty(d):

	if d == 'easy' or d == 'e':
		return 10 
	if d == 'norm' or d == 'n':
		return 1000
	if d == 'hard'or d == 'h':
		return 10000

def menu():	
	print('Hello')
	while True:
		print("+ |sum","- |subtraction",sep='\n')

		try:	
			mode = input()
			if mode == 'exit' or mode == '':
				break
		except ValueError:
			print("Ops,something wrong")
		print("1-100 |easy","100-10000 |norm","1000-100000 |hard",sep='\n')

		try:
			diff = input()
			if diff == 'exit' or diff == '':
				break
		except ValueError:
			print("Ops, something wrong")

		# берём число из функции и добавляем\уменьшаем его на один разряд 
		# Fu*k my English,sorry.	
		if mode == '+':
			main("+",difficulty(diff)/10,difficulty(diff)*10)
		elif mode == '-':
			main("-",difficulty(diff)/10,difficulty(diff)*10)


menu()
