import os

def run(**args):
    print("[*]in invironment module.")
    return str(os.environ)


print(run())
