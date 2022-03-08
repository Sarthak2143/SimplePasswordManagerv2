from datetime import datetime
import sys

path = ".logs/"


def read():
    x = datetime.now()

    day = x.day
    month = x.month
    year = x.year
    hr = x.day
    mn = x.minute
    sec = x.second

    with open(f"{path}/read.log", "a") as r:
        r.write(f"{day}/{month}/{year} {hr}:{mn}:{sec}, Passwords got read.\n")

def write():
    x = datetime.now()
    day = x.day
    month = x.month
    year = x.year
    hr = x.day
    mn = x.minute
    sec = x.second

    with open(f"{path}/write.log", "a") as r:
        r.write(f"{day}/{month}/{year} {hr}:{mn}:{sec}, Passwords wrote down.\n")

def check():
    x = datetime.now()
    day = x.day
    month = x.month
    year = x.year
    hr = x.day
    mn = x.minute
    sec = x.second

    with open(f"{path}/check.log", "a") as r:
        r.write(f"{day}/{month}/{year} {hr}:{mn}:{sec}, Passwords strength got checked.\n")

def generate():
    x = datetime.now()
    day = x.day
    month = x.month
    year = x.year
    hr = x.day
    mn = x.minute
    sec = x.second

    with open(f"{path}/generate.log", "a") as r:
        r.write(f"{day}/{month}/{year} {hr}:{mn}:{sec}, Passwords got generated.\n")
