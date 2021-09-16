import random
from colorama import Fore, Style

time = 5

def sumEasy(): 
    for x in range(time):
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

    with open('stat.txt', 'r+') as f: #r+ does the work of rw
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith('lose'):
                lines[i] = lines[i].strip() + '2012\n'
        f.seek(0)
        for line in lines:
            f.write(line)
        open('stat.txt', 'r+').close()

sumEasy()