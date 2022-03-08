import sys
from getpass import getpass
import src.generate as generate
import src.logs as logs
import src.readwrite as rw
import src.pwdcheck as pwdcheck
import time
from colorama import Fore, Style

def shell():
    while True:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            rw.read()
            logs.read()

        elif choice == 2:
            name = input('Enter account\'s name: ')
            pwd = getpass('Enter password: ')
            rw.write(name, pwd)
            logs.write()

        elif choice == 3:
            generate.pwdgen()
            logs.generate()

        elif choice == 4:
            print('Password strength checker')
            password = input('Enter your password: ')
            print('Checking strength of your password...')
            pwdcheck.checkpwd(password)

            logs.check()

        elif choice == 5:
            print(f"{Fore.BLUE}Exiting...")
            time.sleep(1)
            sys.exit()

        else:
            print("Invalid option")



