import string
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all = lower + upper + digits + symbols

def pwdgen():
    length = int(input("Enter the length for password: "))
    temp = random.sample(all, length)

    password = "".join(temp)

    print(password)

