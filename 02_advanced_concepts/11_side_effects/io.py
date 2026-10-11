import sys

def get_name():
    name = input("Enter your name: ") # side effect: output and input
    print(f"Hello, {name}!")          # side effect: output to console
