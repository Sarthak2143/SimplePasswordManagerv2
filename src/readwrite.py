import time

def read():
    with open('pwds/pwd.txt', 'r') as f:
        print("Reading passwords...")
        time.sleep(1)
        print(f.read())


def write(name, pwd):
    with open("pwds/pwd.txt", "a") as f:
        print("Writing passwords...")
        time.sleep(1)
        f.write(f"\n{name} | {pwd}")

