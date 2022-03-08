### IMPORTS ###

import src.__init__
from src import startup
import random
import time
import os
import sys
from colorama import Fore, Style

### SHELL ###

print(f"Author: {src.__init__.author} | Version: {src.__init__.__version__}")

def main():
    try:
        print(f'{Fore.GREEN}[+] Starting shell...{Style.RESET_ALL}')
        startup.shell()


    except KeyboardInterrupt:
        print(f"\n{Fore.BLUE}Exiting...")
        time.sleep(1)

if __name__ == "__main__":
    main()
