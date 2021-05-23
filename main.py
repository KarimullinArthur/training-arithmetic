import random
from colorama import Fore, Style

while True==True:
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = a + b

    print(a,"+",b,"= ", end='')
    result = input()

    if result == "exit":
        break

    result = int(result)

    if result == c:
        print(Fore.GREEN + 'Right',Style.RESET_ALL)

    else :
        print(Fore.RED + 'Wrong',Style.RESET_ALL, a,"+",b,"=",c)